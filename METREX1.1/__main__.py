import GFS_processor
import BloomSkyForecast
import databuffer
import numpy as np
from scipy import interpolate
import pandas as pd
import time
import sys
import csv

''' Sunnyvale '''
LON = -122.01
LAT = 37.37

Tspan = 24
tmppath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/METREX1.1/datatmp'
filepath = '/home/jiahe/forecast_GFS4_0p50/ModelV1.1_noImage/METREX1.1/dataforecast/'

res = list( BloomSkyForecast.METREX1p1('tmp2m',LON,LAT,tmppath,'0p25',Tspan) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_T2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list( BloomSkyForecast.METREX1p1('tmp2m',LON,LAT,tmppath) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_T2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list( BloomSkyForecast.METREX1p1('rh2m',LON,LAT,tmppath,'0p25',Tspan) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_RH2m_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list( BloomSkyForecast.METREX1p1('rh2m',LON,LAT,tmppath) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_RH2m_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list( BloomSkyForecast.METREX1p1('pressfc',LON,LAT,tmppath,'0p25',Tspan) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_pressfc_GFS0p25.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

res = list( BloomSkyForecast.METREX1p1('pressfc',LON,LAT,tmppath) )
line = (int(time.time()), res)
with open (filepath+'Sunnyvale_pressfc_GFS0p50.csv','a') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(line)

