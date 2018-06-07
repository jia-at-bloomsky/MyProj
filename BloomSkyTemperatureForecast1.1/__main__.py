import GFS_interp
import pandas as pd
import time
import sys
import csv

import getCaiyun

time_now = time.gmtime(int(time.time()))
if time_now.tm_hour%6 > 0:
    sys.exit(0)

''' Sunnyvale '''
LON = -122.01
LAT = 37.37
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Sunnyvale_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Sunnyvale_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Sunnyvale_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' Tianjin '''
LON = 117.13
LAT = 39.11
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Tianjin_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Tianjin_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Tianjin_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Tianjin_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' GuoNengRiXin '''
LON = 100.57
LAT = 36.14
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Guonengrixin_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Guonengrixin_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Guonengrixin_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Guonengrixin_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' Wuhan Happy Valley '''
LON = 114.39
LAT = 30.60
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'HappyValley_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'HappyValley_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'HappyValley_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'HappyValley_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' Zhengguo '''
LON = 103.96
LAT = 23.56
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Zhengguo_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Zhengguo_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Zhengguo_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Zhengguo_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' Hongguo '''
LON = 104.31
LAT = 23.30
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Hongguo_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Hongguo_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Hongguo_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Hongguo_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

''' Xian Haisheng '''
LON = 108.96
LAT = 34.16
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/TestInChina/data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'Haisheng_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'Haisheng_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'Haisheng_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'Haisheng_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)
