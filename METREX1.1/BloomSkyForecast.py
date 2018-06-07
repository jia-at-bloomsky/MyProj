import numpy as np
import pandas as pd
from scipy import interpolate
import time
import GFS_processor
import databuffer

def Prevision1p1(res,var,LON,LAT,Tspan,tmppath):
    if ( LON >= -180 ) and ( LON < 0 ):
        LON = LON + 360

    # obtain spatio-temporal indices on GFS data
    lonidx, latidx, tidx = GFS_processor.index_locator(LON, LAT, Tspan, res).obtIndices()
    lons, lats = GFS_processor.getLONLAT(res)

    # check existence of tmp data file
    for itidx in np.arange(tidx[0],tidx[1]+1):
        if not databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).fileexist()['currentfile']:
            downloader = GFS_processor.GFS_downloader(res,var,[itidx,itidx],
                                                      [0,GFS_processor.GFS_latend()[res]],
                                                      [0,GFS_processor.GFS_lonend()[res]])
            tmpdata = downloader.get_gfs_data() # savetmpfile
            databuffer.DataOnServer(tmppath,res,var,itidx,tmpdata).save()
        if databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).fileexist()['prevfile']:
            databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).delete()

    # spatial interpolation (cubic)
    dataout=[]
    for itidx in np.arange(tidx[0],tidx[1]+1):
        tmpdata = databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).dataload()
        ff = interpolate.interp2d(lons[lonidx[0]:lonidx[1]+1],lats[latidx[0]:latidx[1]+1],
                                  tmpdata[latidx[0]:latidx[1]+1,lonidx[0]:lonidx[1]+1],
                                  kind='cubic')
        dataout.append(ff(LON,LAT).tolist()[0])
        dataout.append(np.nan)
        dataout.append(np.nan)

    # temporal interpolation (linear)
    ff = interpolate.interp1d(np.arange(0,1+(tidx[1]-tidx[0])*3,3),[x for x in dataout if not np.isnan(x)])
    dataout = ff(np.arange(0,1+(tidx[1]-tidx[0])*3,1))

    time_now = time.gmtime(int(time.time()))
    # return dataout[time_now.tm_hour%6:time_now.tm_hour%6+24]
    return dataout
