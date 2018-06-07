import GFS_processor
import BloomSkyForecast
import databuffer
import numpy as np
from scipy import interpolate

''' Sunnyvale '''
LON = -122.01
LAT = 37.37
res = '0p25'
var = 'tmp2m'
Tspan = 24
tmppath = './datatmp'


# lonidx, latidx, tidx = GFS_processor.index_locator(LON, LAT, Tspan, res).obtIndices()
# # print lonidx
# # print latidx
# # print tidx
#
# itidx = tidx[0]
# tmpdata = databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).dataload()
# print np.shape(tmpdata)
# print tmpdata[latidx[0]:latidx[1]+1,lonidx[0]:lonidx[1]+1]

tout = BloomSkyForecast.Prevision1p1(res,var,LON,LAT,Tspan,tmppath)
print tout
# itidx = 2
# tmpdata = databuffer.DataOnServer(tmppath,res,var,itidx,np.nan).dataload()
# print tmpdata[latidx[0]:latidx[1]+1,lonidx[0]:lonidx[1]+1]