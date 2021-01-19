import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..","..."))
from configparser import ConfigParser

#Create Object
config = ConfigParser()

#Read Data

def readConfigData(section,content):
    config.read("./configfiles/config.cfg")
    return config.get(section,content)