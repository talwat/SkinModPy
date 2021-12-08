from json import loads
import methods

def getSkin(name, outputPath):
    uuid = ""
    try:
        methods.log("Getting name profile info...")
        rawNameData = methods.getFromInternet("https://api.mojang.com/users/profiles/minecraft/{}".format(name))
    except Exception as e:
        methods.log("An error occured while downloading the skin: {}.".format(str(e)), "fatal")
        return "error"

    if(len(rawNameData) > 0):
        methods.log("Loading raw name profile info into json...")
        userInfo = loads(rawNameData)
        uuid = userInfo["id"]
    else:
        return "404"
    
    methods.log("Getting full profile info with uuid...")
    rawUuidData = methods.getFromInternet("https://sessionserver.mojang.com/session/minecraft/profile/{}".format(uuid))
    methods.log("Loading raw uuid info into json...")
    uuidData = loads(rawUuidData)
    encodedRawSkinData = uuidData["properties"][0]["value"]
    methods.log("Decoding raw skin data...")
    decodedRawskinData = methods.base64Decode(encodedRawSkinData)
    methods.log("Loading raw skin data into json...")
    skinData = loads(decodedRawskinData)
    skinUrl = skinData["textures"]["SKIN"]["url"]
    methods.log("Downloading skin file from the Mojang API...")
    methods.downloadFile(skinUrl, outputPath)
    methods.log("Downloaded skin file!", "success")
    return "success"