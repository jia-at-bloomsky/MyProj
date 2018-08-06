import pandas as pd
import numpy as np
import pytz
from datetime import datetime, timedelta

def sdp_avails(cur):
    cur.execute("SELECT organization_id, sdp_id, device_type FROM sdp_list WHERE status=1")
    sdps = pd.DataFrame( list(cur.fetchall()) )
    orgs = list(sdps['organization_id'].unique())
    spots = list(sdps['sdp_id'][sdps['device_type']=='spot'].unique())
    rainbuckets = list(sdps['sdp_id'][sdps['device_type']=='rainbucket'].unique())
    return orgs, spots, rainbuckets

def sdp_online_pct(session,sdp_list,device_type,localdate):
    if device_type == 'spot':
        statement = session.prepare('''SELECT * FROM archive_spot_data WHERE date=? AND sdp_id=?''')
    elif device_type == 'rainbucket':
        statement = session.prepare('''SELECT * FROM archive_rainbucket_data WHERE date=? AND sdp_id=?''')
    else:
        print "Wrong Input Device Type:  "+device_type
        exit(0)

    sdp_count = 0
    for sdp in sdp_list:
        if session.execute(statement,(localdate,sdp)):
            sdp_count = sdp_count + 1

    if len(sdp_list)==0:
        return
    return round(float(sdp_count)/float(len(sdp_list)), 2)


class organization_info():
    def __init__(self,session,org_id):
        self.session = session
        self.org_id = org_id

    def org_info(self):
        org = pd.DataFrame(list(self.session.execute('''SELECT * FROM organization WHERE organization_id=%s''',
                                                     [self.org_id])))
        return org.organization_name[0], org.email[0], \
               datetime.utcfromtimestamp(org.created_at[0]).replace(tzinfo=pytz.utc).\
                   astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')

    def group_info(self):
        group = pd.DataFrame(list(self.session.execute('''SELECT * FROM organization_group WHERE 
        organization_id=%s''',[self.org_id])))
        group_sdp = pd.DataFrame(list(self.session.execute('''SELECT * FROM organization_group_sdp WHERE 
        organization_id=%s''',[self.org_id])))
        return group,group_sdp

    def device_info(self):
        device = pd.DataFrame(list(self.session.execute('''SELECT device_id, device_model, sdp_id, sdp_type, 
        created_at, lon, lat, utc FROM organization_sdp WHERE
        organization_id=%s''',[self.org_id])))
        return device

class device_info():
    def __init__(self,session,sdp_id):
        self.session = session
        self.sdp_id = sdp_id

    def __basicinfo(self):
        device = pd.DataFrame(list(self.session.execute('''SELECT device_id, device_model, sdp_id, sdp_type, sdp_name, 
        created_at, lon, lat, utc FROM sdp WHERE sdp_id=%s''', [self.sdp_id])))
        device['create_date'] = device['created_at'].apply(
            lambda x: datetime.utcfromtimestamp(device.created_at).replace(tzinfo=pytz.utc).
                astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
        )
        return device

    def __all_dates(self):
        basicinfo = self.__basicinfo()
        create_date = datetime.utcfromtimestamp(basicinfo.created_at).date()
        localdate = (datetime.today()-timedelta(days=1)).replace(tzinfo=pytz.utc).\
            astimezone(pytz.timezone('Asia/Shanghai')).date()
        dates = [create_date+timedelta(days=i) for i in np.arange(1+(localdate-create_date).days)]

        if str(basicinfo.sdp_type[0]) == 'spot':
            statement = self.session.prepare('''SELECT date FROM archive_spot_data WHERE date=? AND sdp_id=?''')
        elif str(basicinfo.sdp_type[0]) == 'rainbucket':
            statement = self.session.prepare('''SELECT date FROM archive_rainbucket_data WHERE date=? AND sdp_id=?''')
        else:
            print "Wrong Input Device Type:  " + basicinfo.sdp_type
            exit(0)

        datadates = []
        for idate in dates:
            self.session.execute(statement,(str(idate),self.sdp_id))
            tmp = list(self.session.execute(statement,(str(idate),self.sdp_id)))
            if tmp:
                datadates = datadates + pd.DataFrame(tmp).date.unique().tolist()

        return datadates

    def __checkversion(self):
        basicinfo = self.__basicinfo()
        datadates = self.__all_dates()
        if str(basicinfo.sdp_type[0]) == 'spot':
            statement = self.session.prepare('''SELECT version FROM archive_spot_data WHERE date=? AND sdp_id=?''')
        elif str(basicinfo.sdp_type[0]) == 'rainbucket':
            statement = self.session.prepare('''SELECT version FROM archive_rainbucket_data WHERE date=? AND sdp_id=?''')
        else:
            print "Wrong Input Device Type:  " + basicinfo.sdp_type
            exit(0)

        if not datadates:
            return []
        if len(datadates)==1:
            return [pd.DataFrame(list(self.session.execute(statement,(datadates[0],self.sdp_id)))).version.tolist()[-1]]
        if len(datadates)>1:
            return [pd.DataFrame(list(self.session.execute(statement,(datadates[-1],self.sdp_id)))).version.tolist()[-1],\
                    pd.DataFrame(list(self.session.execute(statement,(datadates[-2],self.sdp_id)))).version.tolist()[-1]]

    def __checkLocChange(self):
        localdate = (datetime.today() - timedelta(days=1)).replace(tzinfo=pytz.utc). \
            astimezone(pytz.timezone('Asia/Shanghai')).date()
        tmp = list(self.session.execute('''SELECT * FROM location_change_log WHERE sdp_id=%s''',
                                        [self.sdp_id]))
        if not tmp:
            return 0
        if datetime.utcfromtimestamp(pd.DataFrame(tmp).ts.max()).date() == localdate:
            return 1

    def device_monitor(self):
        basicinfo = self.__basicinfo()
        datadates = self.__all_dates()
        firmwares = self.__checkversion()

        localdate = str((datetime.today() - timedelta(days=1)).
                        replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai')).date())

        lendates = len(datadates)
        if datadates:
            datadates = datadates[-1]
        else:
            datadates = 9999

        if len(firmwares) == 1:
            firmupdate = 0
        elif len(firmwares) == 2:
            if firmwares[0] == firmwares[1]:
                firmupdate = 0
            else:
                firmupdate = 1
        else:
            firmupdate = 9999
            firmwares = [9999]

        return localdate, basicinfo.device_id[0], basicinfo.device_model[0], basicinfo.sdp_id[0], basicinfo.sdp_type[0], \
               basicinfo.create_date[0], datadates, lendates, basicinfo.lon[0], basicinfo.lat[0], \
               firmwares[0], self.__checkLocChange(), firmupdate, float(basicinfo.utc[0]), basicinfo.sdp_name[0], \
               str(datadates==localdate)


