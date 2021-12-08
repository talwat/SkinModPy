import json
import methods

rawFiles = ""
files = ""
fileNames = []

def init():
    rawFiles = methods.getFromInternet("https://api.github.com/repos/talwhat/SkinModPy-Database/contents/overlays?ref=master")
    files = json.loads(rawFiles)
    for file in files:
        fileNames.append(file["name"])