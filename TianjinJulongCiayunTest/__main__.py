import sys
sys.path.insert(0, "/Users/jiahe/PycharmProjects/BloomSkyTemperatureForecast1.1")

import GFS_interp
import time
import csv
import getCaiyun

time_now = time.gmtime(int(time.time()))
if time_now.tm_hour%6 > 0:
    sys.exit(0)

LON = 114.5
LAT = -3
filepath = './data_/'

res = list(GFS_interp.GFS_interp('0p25','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','tmp2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','rh2m',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p25','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list(GFS_interp.GFS_interp('0p50','pressfc',LON,LAT,[2,12]))
line = (int(time.time()), res)
with open (filepath+'IN_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'temperature'))
with open (filepath+'IN_T2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'humidity'))
with open (filepath+'IN_RH2m_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

line = (int(time.time()), getCaiyun.getCaiyun(LON,LAT,'pres'))
with open (filepath+'IN_pressfc_Caiyun.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)
