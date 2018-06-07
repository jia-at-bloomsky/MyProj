import time
import requests
import numpy as np
from scipy import interpolate
from datetime import datetime
import os
import csv

def GFS0p50_locateLON(LON):
    ''' verify LON range '''
    if (LON >= -180) and (LON < 0):
        LON = LON + 360
    elif (LON >= 0) and (LON <= 360):
        LON = LON
    else:
        print
        "LON out of range"
        return np.nan

    ''' locate LON '''
    if int(LON) % 2 == 1:
        return [int(LON) * 2 - 2, int(LON) * 2 + 2]
    else:
        return [int(LON) * 2, int(LON) * 2 + 4]


def GFS0p50_locateLAT(LAT):
    ''' verify LAT range '''
    if (LAT > 90) or (LAT < -90):
        print
        "LAT out of range"
        return np.nan

    ''' locate LAT '''
    if int(LAT + 90) % 2 == 1:
        return [int(LAT + 90) * 2 - 2, int(LAT + 90) * 2 + 2]
    else:
        return [int(LAT + 90) * 2, int(LAT + 90) * 2 + 4]


def GFS0p25_locateLON(LON):
    ''' verify LON range '''
    if (LON >= -180) and (LON < 0):
        LON = LON + 360
    elif (LON >= 0) and (LON <= 360):
        LON = LON
    else:
        print
        "LON out of range"
        return np.nan

    ''' locate LON '''
    return [int(LON) * 4, int(LON) * 4 + 4]


def GFS0p25_locateLAT(LAT):
    ''' verify LAT range '''
    if (LAT > 90) or (LAT < -90):
        print
        "LAT out of range"
        return np.nan

    ''' locate LAT '''
    return [int(LAT + 90) * 4, int(LAT + 90) * 4 + 4]