import time
import requests
import numpy as np
from scipy import interpolate
import GFS_downloader
import GFS_locator
from datetime import datetime
import os
import csv

def GFS_interp( res, var, LON, LAT, tidx ):

    if ( LON >= -180 ) and ( LON < 0 ):
        LON = LON + 360

    if res == '0p50':
        lons = np.arange( 0, 360.1, 0.5 )
        lats = np.arange( -90, 90.1, 0.5 )
        lonidx = GFS_locator.GFS0p50_locateLON(LON)
        latidx = GFS_locator.GFS0p50_locateLAT(LAT)
        downloader = GFS_downloader.GFS0p50_downloader(var, tidx, latidx, lonidx)

    elif res == '0p25':
        lons = np.arange( 0, 360.1, 0.25 )
        lats = np.arange( -90, 90.1, 0.25 )
        lonidx = GFS_locator.GFS0p25_locateLON(LON)
        latidx = GFS_locator.GFS0p25_locateLAT(LAT)
        downloader = GFS_downloader.GFS0p25_downloader(var, tidx, latidx, lonidx)

    else:
        print "Invalid Resolution: " + res
        return np.nan

    TF = []

    tmpdata = downloader.get_gfs_data()
    print tmpdata[0]
    for it in np.arange(tidx[1]-tidx[0]+1):
        ff = interpolate.interp2d(lons[lonidx[0]:lonidx[1]+1], lats[latidx[0]:latidx[1]+1], tmpdata[it], kind = 'cubic' )
        TF.append ( ff(LON, LAT).tolist()[0] )
        if it == 0:
            print lons[lonidx[0]:lonidx[1] + 1]
            print lats[latidx[0]:latidx[1] + 1]
            print tmpdata[it]
            print LON, LAT
            print ff(LON, LAT).tolist()[0]
        if it==tidx[1]-tidx[0]:
            break
        TF.append(np.nan)
        TF.append(np.nan)
    print TF

    ff = interpolate.interp1d( np.arange(0,31,3), [x for x in TF if str(x) != 'nan'])
    TF = ff( np.arange(0,31,1) )
    print TF
    return TF