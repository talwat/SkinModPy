import json
import methods

rawFiles = ""
files = ""
fileNames = []

def init():
    methods.log("Viewing raw overlays info from the Github API...")
    rawFiles = methods.getFromInternet("https://api.github.com/repos/talwhat/SkinModPy-Database/contents/overlays?ref=master")
    methods.log("Loading raw overlays info into json...")
    files = json.loads(rawFiles)
    methods.log("Loading all overlay names into a list...")
    for file in files:
        fileNames.append(file["name"])
    methods.log("Done getting info from the Github API!", "success")