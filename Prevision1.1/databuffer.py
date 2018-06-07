import time
import numpy as np
import pandas as pd
import os.path
import os
import sys
class DataOnServer():
    def __init__(self,tmppath,res,var,itidx,data):
        self.tmppath = tmppath
        self.res = res
        self.var = var
        self.itidx = itidx
        self.data = data
        self.time_now = time.gmtime(int(time.time()))
        self.time_currentfile = time.gmtime(int(time.time())-(self.time_now.tm_hour%6)*3600)
        self.time_prevfile = time.gmtime(int(time.time())-(6+self.time_now.tm_hour%6)*3600)

    def __current_filename__(self): # create filename for the current tmp file
        return self.var+'_'+str(self.time_currentfile.tm_year)+str(self.time_currentfile.tm_mon)+\
               str(self.time_currentfile.tm_mday)+'_'+str(self.time_currentfile.tm_hour)+'_'+\
               self.res+'_'+str(self.itidx)+'.csv'

    def __prev_filename__(self): # create filename for the previous tmp file to delete
        return self.var+'_'+str(self.time_prevfile.tm_year)+str(self.time_prevfile.tm_mon)+\
               str(self.time_prevfile.tm_mday)+'_'+str(self.time_prevfile.tm_hour)+'_'+\
               self.res+'_'+str(self.itidx)+'.csv'

    def fileexist(self): # determine the existence of the current and previous tmp file
        return {
            'currentfile': os.path.exists(self.tmppath+'/'+self.__current_filename__()),
            'prevfile': os.path.exists(self.tmppath+'/'+self.__prev_filename__())
        }

    def save(self): # save the current file
        if not self.fileexist()['currentfile']:
            pd.DataFrame(np.array(self.data)[0]).to_csv(self.tmppath+'/'+self.__current_filename__(),index=False)

    def delete(self): # delete the prev file
        if self.fileexist()['prevfile']:
            os.remove(self.tmppath+'/'+self.__prev_filename__())

    def dataload(self):
        if not self.fileexist()['currentfile']:
            print self.__current_filename__() + " not exist"
            sys.exit(0)
        else:
            return np.array(pd.read_csv(self.tmppath+'/'+self.__current_filename__()))

