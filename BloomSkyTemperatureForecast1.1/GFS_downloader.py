import time
import requests
import numpy as np
from scipy import interpolate
from datetime import datetime
import os
import csv

class GFS0p50_downloader():
    def __init__(self, varname, tidx, latidx, lonidx):
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
        if self.lonidx[1] == 720:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_0p50/gfs{}/gfs_0p50_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
                                                  self.latidx[0], self.latidx[1], self.lonidx[0], 719),
                   'http://nomads.ncep.noaa.gov:9090/dods/gfs_0p50/gfs{}/gfs_0p50_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
                                                  self.latidx[0], self.latidx[1], 0, 0)]
        else:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_0p50/gfs{}/gfs_0p50_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
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



class GFS0p25_downloader():
    def __init__(self, varname, tidx, latidx, lonidx):
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
        if self.lonidx[1] == 720:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_0p25/gfs{}/gfs_0p25_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
                                                  self.latidx[0], self.latidx[1], self.lonidx[0], 719),
                   'http://nomads.ncep.noaa.gov:9090/dods/gfs_0p25/gfs{}/gfs_0p25_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
                                                  self.latidx[0], self.latidx[1], 0, 0)]
        else:
            url = ['http://nomads.ncep.noaa.gov:9090/dods/gfs_0p25/gfs{}/gfs_0p25_{}z.ascii?{}' \
                   '[{}:{}][{}:{}][{}:{}]'.format(yyyymmdd, cc, self.varname, self.tidx[0], self.tidx[1], \
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