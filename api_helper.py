from NorenRestApiPy.NorenApi import NorenApi
from threading import Timer
import pandas as pd
import time

class SymbolItem:
    def __init__(self):
        self.df = None
        self.key = None
        self.counter  = 0
        self.lasttime = 0    

def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)


class StarApiPy(NorenApi):
    
    def __init__(self, *args, **kwargs):
        super(StarApiPy, self).__init__(host='https://starapiuat.prostocks.com/NorenWClientTP', websocket='wss://starapiuat.prostocks.com/NorenWS/')
        
    