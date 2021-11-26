from json import loads
import methods

def getSkin(name, outputPath):
    uuid = ""
    rawNameData = methods.getFromInternet("https://api.mojang.com/users/profiles/minecraft/{}".format(name))

    if(len(rawNameData) > 0):
        userInfo = loads(rawNameData)
        uuid = userInfo["id"]
        
    else:
        return "error"
    
    rawUuidData = methods.getFromInternet("https://sessionserver.mojang.com/session/minecraft/profile/{}".format(uuid))
    uuidData = loads(rawUuidData)
    encodedRawSkinData = uuidData["properties"][0]["value"]
    decodedRawskinData = methods.base64Decode(encodedRawSkinData)
    skinData = loads(decodedRawskinData)
    skinUrl = skinData["textures"]["SKIN"]["url"]
    methods.downloadFile(skinUrl, outputPath)
    return "success"