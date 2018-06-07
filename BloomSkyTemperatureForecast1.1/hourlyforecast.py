import numpy as np
import pandas as pd
import time
import GFS_downloader
import GFS_locator
from scipy import interpolate
import os.path


def obt_tidx(Tspan):
    return {
        24: [2,12],
        72: [2,28]
    }[Tspan]

def write_tmpfilename(var,res,itidx):
    time_now = time.gmtime(int(time.time()))
    time_now = time.gmtime(int(time.time())-(time_now.tm_hour%6)*3600)
    return str( var+'_'+str(time_now.tm_year)+str(time_now.tm_mon)+str(time_now.tm_mday)+\
           '_'+str(time_now.tm_hour)+'_'+res+'_'+str(itidx)+'.csv' )

def tmpdatadownload(tmppath, res, var, Tspan):
    tidx = obt_tidx(Tspan)
    time_now = time.gmtime(int(time.time()))
    if True: #time_now.tm_hour%6 == 0:
        for itidx in np.arange(tidx[0],tidx[1]+1,1):
            tmpfilename = write_tmpfilename(var,res,itidx)
            if not os.path.exists(tmppath+'/'+tmpfilename):
                downloader = GFS_downloader.GFS_downloader(res, var, [itidx,itidx], [0,360], [0,720])
                tmpdata = downloader.get_gfs_data()
                pd.DataFrame(np.array(tmpdata)[0]).to_csv(tmppath+'/'+tmpfilename, index=False)

def hourlyforecast( tmppath, res, var, LON, LAT, Tspan ):
    time_now = time.gmtime(int(time.time()))

    tidx = obt_tidx(Tspan)

    if True: #time_now.tm_hour%6 == 0:
        tmpdatadownload(tmppath, res, var, Tspan)

    if res == '0p50':
        lons = np.arange(0, 360.1, 0.5)
        lats = np.arange(-90, 90.1, 0.5)
        lonidx = GFS_locator.GFS0p50_locateLON(LON)
        latidx = GFS_locator.GFS0p50_locateLAT(LAT)
    elif res == '0p25':
        lons = np.arange(0, 360.1, 0.25)
        lats = np.arange(-90, 90.1, 0.25)
        lonidx = GFS_locator.GFS0p25_locateLON(LON)
        latidx = GFS_locator.GFS0p25_locateLAT(LAT)
    else:
        print ("Invalid Resolution: " + res)
        return np.nan

    dataout = []
    for i, itidx in enumerate( np.arange(tidx[0],tidx[1]+1,1)) :
        tmpfilename = write_tmpfilename(var,res,itidx)
        tmpdata = np.array( pd.read_csv(tmppath+'/'+tmpfilename) )
        ff = interpolate.interp2d(lons[lonidx[0]:lonidx[1]+1],lats[latidx[0]:latidx[1]+1],
                                  tmpdata[latidx[0]:latidx[1]+1,lonidx[0]:lonidx[1]+1],
                                  kind='cubic')
        dataout.append( ff(LON,LAT).tolist()[0] )
        # if i==tidx[1]-tidx[0]:
        #     break
        dataout.append(np.nan)
        dataout.append(np.nan)

    ff = interpolate.interp1d( np.arange(0,1+(tidx[1]-tidx[0])*3,3), [x for x in dataout if not np.isnan(x)] )
    dataout = ff( np.arange(0,1+(tidx[1]-tidx[0])*3,1) )

    return dataout[time_now.tm_hour%6:time_now.tm_hour%6+24]


