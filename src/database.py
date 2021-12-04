import methods

url = "https://raw.githubusercontent.com/talwhat/SkinModPy-Database/master/"

def getOverlay(name):
    try:
        overlayURL = url + name
        methods.downloadFile(overlayURL, "downloadedOverlay.png")
        return "success"
    except Exception as e:
        if("404" in str(e)):
            return "404"
        else:
            return "error"