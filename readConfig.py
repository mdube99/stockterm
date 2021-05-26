from configparser import ConfigParser

def getData(ConfigData):
    config = ConfigParser()
    config.read('config.ini')
    rdata = config.get(ConfigData,'api_key')
    return rdata 
