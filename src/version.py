from json import loads
from methods import getFromInternet

version = "1.3"
latestVersion = version

def versionGet():
    try:
    	programInfo = loads(getFromInternet("https://raw.githubusercontent.com/talwat/SkinModPy/master/program.json"))
    except:
    	programInfo = {}

    if(programInfo != {}):
       return programInfo["version"]
    else:
        return version