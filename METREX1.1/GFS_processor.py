import time
import requests
import numpy as np
from scipy import interpolate
from datetime import datetime
import os
import csv

def GFS_lonend():
    ''' dimension of longitude data for the two dif resolutions  '''
    return{
        '0p50':720,
        '0p25':1440
    }

def GFS_latend():
    ''' dimension of latitude data for the two dif resolutions  '''
    return{
        '0p50':360,
        '0p25':720
    }

class GFS_downloader():
    ''' download GFS data given resolution, variable, temporal and spatial indices:

    res is GFS resolution, '0p50' or '0p25';

    varname is the variable name in GFS archive, 'tmp2m' for temperature at 2 meters above ground, etc.;

    tidx in form of [ti0, ti1] representing the starting and ending indices in time, ti0==ti1 if just ONE time point is needed;

    latidx in form of [lati0, lati1] representing the starting and ending indices in latitudes, lati0==lati1 if just ONE latitude is needed;

    lonidx in form of [loni0, loni1] representing the starting and ending indices in longitudes, loni0==loni1 if just ONE longitude is needed;

    '''

    def __init__(self, res, varname, tidx, latidx, lonidx):
        self.res = res
        self.varname = varname
        self.tidx = tidx
        self.latidx = latidx
        self.lonidx = lonidx

    def __get_utc_time_minus_6_hours(self):
        time_now = time.gmtime(int(time.time()) - 3600 * 6)
        year = str(time_now.tm_year)
        month = '{month:02d}'.format(month=time_now.tm_mon)
        day = '{day:02d}'.format(day=time_now.tm_mday)
        hour = '{hour:02d}'.format(hour=time_now.tm_hour)
        return year, month, day, hour

    def __prepare_parameters(self):
        year, month, day, hour = self.__get_utc_time_minus_6_hours()
        yyyymmdd = year + month + day
        if hour >= '00' and hour < '06':
            cc = '00'
        elif hour >= '06' and hour < '12':
            cc = '06'
        elif hour >= '12' and hour < '18':
            cc = '12'
        elif hour >= '18' and hour < '24':
            cc = '18'
        if self.lonidx[1] == GFS_lonend()[self.res]:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_{}/gfs{}/gfs_{}_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(self.res, yyyymmdd, self.res, cc, self.varname, self.tidx[0], \
                                                  self.tidx[1], self.latidx[0], self.latidx[1], self.lonidx[0], \
                                                  GFS_lonend()[self.res]-1),
                   'http://nomads.ncep.noaa.gov:9090/dods/gfs_{}/gfs{}/gfs_{}_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(self.res, yyyymmdd, self.res, cc, self.varname, self.tidx[0], \
                                                  self.tidx[1], self.latidx[0], self.latidx[1], 0, 0)]
        else:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_{}/gfs{}/gfs_{}_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(self.res, yyyymmdd, self.res, cc, self.varname, self.tidx[0], self.tidx[1], \
                                                  self.latidx[0], self.latidx[1], self.lonidx[0], self.lonidx[1])]
        return url

    def __process_raw_data(self, data):
        data = data.splitlines()
        tmpdata = []
        tt = []
        for line in data:
            if 'time' in line:
                break
            if self.varname in line:
                continue
            if line != '':
                tmpdata.append([float(i) for i in line.split(', ')[1:]])
            if line == '':
                tt.append(tmpdata)
                tmpdata = []
        return filter(None, tt)

    def get_gfs_data(self):
        url = self.__prepare_parameters()
        headers = {'Content-type': 'application/json;charset=utf8'}
        if len(url) == 1:
            r = requests.get(url[0], headers=headers)
            data = self.__process_raw_data(r.text)
            return data
        else:
            r = requests.get(url[0], headers=headers)
            data1 = self.__process_raw_data(r.text)
            r = requests.get(url[1], headers=headers)
            data2 = self.__process_raw_data(r.text)
            data = []
            for j in np.arange(self.tidx[1] - self.tidx[0] + 1):
                tmp = []
                for i in np.arange(self.latidx[1] - self.latidx[0] + 1):
                    tmp.append(data1[j][i] + data2[j][i])
                data.append(tmp)
            return data

class index_locator():
    ''' 
    locate the indice for longitude/latitude/time ranges
    '''

    def __init__(self,LON,LAT,Tspan,res):
        self.LON = LON
        self.LAT = LAT
        self.Tspan = Tspan
        self.res = res

    def __getLONidx__(self):
        if (self.LON >= -180) and (self.LON < 0):
            self.LON = self.LON + 360
        elif (self.LON >= 0) and (self.LON <= 360):
            self.LON = self.LON
        else:
            print "LON out of range"
            return np.nan

        if self.res == '0p25':
            return [int(self.LON)*4, int(self.LON)*4+4]
        elif self.res == '0p50':
            if int(self.LON) % 2 == 1:
                return [int(self.LON)*2-2, int(self.LON)*2+2]
            else:
                return [int(self.LON)*2, int(self.LON)*2+4]
        else:
            print "invalid resolution"
            return np.nan

    def __getLATidx__(self):
        if (self.LAT>90) or (self.LAT<-90):
            print "LAT out of range"
            return np.nan

        if self.res == '0p25':
            return [int(self.LAT+90)*4, int(self.LAT+90)*4+4]
        elif self.res == '0p50':
            if int(self.LAT+90)%2 == 1:
                return [int(self.LAT+90)*2-2, int(self.LAT+90)*2+2]
            else:
                return [int(self.LAT+90)*2, int(self.LAT+90)*2+4]
        else:
            print "invalid resolution"
            return np.nan

    def __getTidx__(self):
        return {
            24: [2,12],
            72: [2,28]
        }[self.Tspan]

    def obtIndices(self):
        lonidx = self.__getLONidx__()
        latidx = self.__getLATidx__()
        tidx = self.__getTidx__()
        return lonidx,latidx,tidx

def getLONLAT(res):
    '''
    get longitudes/latitudes for dif resolutions
    '''
    if res == '0p25':
        return np.arange(0, 360.1, 0.25), np.arange(-90, 90.1, 0.25)
    elif res == '0p50':
        return np.arange(0, 360.1, 0.5), np.arange(-90, 90.1, 0.5)
    else:
        print("Invalid Resolution: " + res)
        return np.nan, np.nan

