import configparser
from pathlib import Path

configFile = 'test.ini'
configFolder = 'config'

config = configparser.ConfigParser()

Config_File = Path(__file__).parent.parent.joinpath(configFolder).joinpath(configFile)
config.read(Config_File)
print(configFile)

def getPetApiUrl():
    return (config['pet']['url'])


