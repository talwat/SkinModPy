import methods

url = "https://raw.githubusercontent.com/talwhat/SkinModPy-Database/master/"

def getOverlay(name):
    try:
        overlayURL = url + name
        methods.downloadFile(overlayURL, "downloadedOverlay.png")
        methods.log("Downloaded overlay file!", "success")
        return "success"
    except Exception as e:
        if("404" in str(e)):
            return "404"
        else:
            methods.log("An error occured while downloading the overlay: {}.".format(str(e)), "fatal")
            return "error"