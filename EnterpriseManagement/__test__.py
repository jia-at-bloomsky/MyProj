from DB_connector import setup_connection, mysql_connection
from EnterpriseMonitoring import *
# import logging
from datetime import datetime, timedelta
import pytz

if datetime.now().replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai')).hour != 1:
    exit(0)

# set up Cassandra connection
try:
    client, session = setup_connection()
except:
    print('Failed to connect to Cassandra')
    exit(0)

# set up MySQL connection
try:
    conn, cur = mysql_connection()
except:
        print('Failed to connect to MySQL')
        exit(0)

# get all active orgs and devices from sdp_list table
orgs_id, spots_sdp, rainbuckets_sdp = sdp_avails(cur)
# double check the existence of orgs_sdp, spots_sdp, rainbuckets_sdp in tables

# table: log_super_admin
localdate = str( ( datetime.today()-timedelta(days=1) ).
                 replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai')).date() )
# monitor system updates at 00:05AM each day, archive stats for the previous day
super_admin_name = 'yang'
num_all_organizations = len(orgs_id)
num_all_spots = len(spots_sdp)
num_all_rainbuckets = len(rainbuckets_sdp)
pct_online_spots = sdp_online_pct(session,spots_sdp,'spot',localdate)
pct_online_rainbuckets = sdp_online_pct(session,rainbuckets_sdp,'rainbucket',localdate)

cur.execute(
    '''INSERT INTO log_super_admin (
    date, super_admin_name, num_all_organizations, num_all_spots,
    num_all_rainbuckets, pct_online_spots, pct_online_rainbuckets
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)''',
    (localdate,super_admin_name,num_all_organizations,num_all_spots,num_all_rainbuckets,
     pct_online_spots,pct_online_rainbuckets)
)
conn.commit()

# table
for org_id in orgs_id:
    org = organization_info(session,org_id)
    name, email, org_create_date = org.org_info()
    group, group_sdp = org.group_info()
    device = org.device_info()
    device = device[device.sdp_id.isin(spots_sdp+rainbuckets_sdp)]
    num_spots = sum(device['sdp_type']=='spot')
    num_rainbuckets = sum(device['sdp_type']=='rainbucket')
    pct_online_spots = sdp_online_pct(session, device.sdp_id[device.sdp_type=='spot'].tolist(), 'spot', localdate)
    pct_online_rainbuckets = sdp_online_pct(session, device.sdp_id[device.sdp_type=='rainbucket'].tolist(),
                                            'rainbucket', localdate)

    cur.execute(
        '''INSERT INTO log_organization (
        date, organization_name, organization_id, email, create_date, num_organization_group, 
        num_spots, num_rainbuckets, pct_online_spots, pct_online_rainbuckets) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
        (localdate,name,org_id,email,org_create_date,group.shape[0],num_spots,num_rainbuckets,pct_online_spots,
         pct_online_rainbuckets)
    )
    conn.commit()

    for idx, idevice in device.iterrows():
        if idevice.sdp_type == 'spot':
            cur.execute(
                '''INSERT INTO log_spot_daily (
                date, device_id, device_model, sdp_id, sdp_type, create_date, lastdata_date, days_online, lon, lat,
                firmware_version, location_update, firmware_update, utc, sdp_name, organization_id, organization_name)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                device_info(session, idevice.sdp_id).device_monitor()+(org_id,name)
            )
        elif idevice.sdp_type == 'rainbucket':
            cur.execute(
                '''INSERT INTO log_rainbucket_daily (
                date, device_id, device_model, sdp_id, sdp_type, create_date, lastdata_date, days_online, lon, lat,
                firmware_version, location_update, firmware_update, utc, sdp_name, organization_id, organization_name)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                device_info(session, idevice.sdp_id).device_monitor()+(org_id,name)
            )
        else:
            print
            "Wrong Input Device Type:  " + idevice.sdp_type
            exit(0)

        conn.commit()

    if group.empty:
        continue

    for idx, row in group.iterrows():
        create_date = datetime.utcfromtimestamp(row.created_at).replace(tzinfo=pytz.utc).\
            astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
        current_device = group_sdp[group_sdp.group_id==row.group_id]
        num_spots = sum(current_device.sdp_type=='spot')
        num_rainbuckets = sum(current_device.sdp_type=='rainbucket')
        pct_online_spots = sdp_online_pct(session, current_device.sdp_id[current_device.sdp_type == 'spot'].tolist(),
                                          'spot', localdate)
        pct_online_rainbuckets = sdp_online_pct(session,
                                                current_device.sdp_id[current_device.sdp_type == 'rainbucket'].tolist(),
                                                'rainbucket', localdate)

        cur.execute(
            '''INSERT INTO log_organization_group (
            date, organization_name, organization_id, group_name, group_id, create_date,
            num_spots, num_rainbuckets, pct_online_spots, pct_online_rainbuckets) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (localdate,name,org_id,row.group_name,row.group_id,create_date,
            num_spots,num_rainbuckets,pct_online_spots,pct_online_rainbuckets)
        )
        conn.commit()


