import json
import urllib.request
import base64

from overlay import downloadFile

def getFromInternet(url):
    result = ""
    file = urllib.request.urlopen(url)
    for line in file:
	    decoded_line = line.decode("utf-8")
	    result += decoded_line
    return result

def base64Decode(input):
    base64_bytes = input.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

def getSkin(name, outputPath):
    uuid = ""
    rawNameData = getFromInternet("https://api.mojang.com/users/profiles/minecraft/{}".format(name))

    if(len(rawNameData) > 0):
        userInfo = json.loads(rawNameData)
        uuid = userInfo["id"]
        
    else:
        return "error"
    
    rawUuidData = getFromInternet("https://sessionserver.mojang.com/session/minecraft/profile/{}".format(uuid))
    uuidData = json.loads(rawUuidData)
    encodedRawSkinData = uuidData["properties"][0]["value"]
    decodedRawskinData = base64Decode(encodedRawSkinData)
    skinData = json.loads(decodedRawskinData)
    skinUrl = skinData["textures"]["SKIN"]["url"]
    downloadFile(skinUrl, outputPath)
    return "success"
