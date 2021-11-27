import os 
import mojang
import methods
import overlayDownload

def main(overlayInput, nameOrFileInput, nameOrPathInput):
    def delTemp():
        if os.path.isdir("skinmodpy-temp"):
            methods.log("Removing temp directory...")
            from shutil import rmtree
            rmtree("skinmodpy-temp")

    if not os.path.isdir("overlays"):
        methods.log("Overlays directory not found.", "error")
        overlayDownload.main()
    overlayInputParsed = methods.parse(overlayInput)
    if(os.path.isfile("overlays/{}.png".format(overlayInputParsed))):
        overlayPath = overlayInputParsed
    else:
        methods.log("Overlay not found.", "fatal")
        return "error.overlay"
    nameOrFile = nameOrFileInput
    path = ""
    if(nameOrFile == "n" or nameOrFile == "name"):
        if not os.path.isdir("skinmodpy-temp"):
            methods.log("Making temp directory...");
            os.mkdir("skinmodpy-temp")
        methods.log("Downloading skin...")
        if not(mojang.getSkin(nameOrPathInput, "temp/skin.png") == "success"):
            methods.log("User not found.", "fatal")
            delTemp()
            return "error.skinGet"
        else:
            path = "skinmodpy-temp/skin.png"
    else:
        if os.path.isfile(nameOrPathInput):
            path = nameOrPathInput
        else:
            methods.log("The file couldn't be found.", "fatal")
            delTemp()
            return "error.path"
    
    if os.path.isfile(path):
        methods.log("Overlaying images...");
        methods.overlayImage(path, "overlays/{}.png".format(overlayPath), "output.png")
        delTemp()
        methods.log("Done!", "success")
        return "success"
    else:
        methods.log("The path couldn't be found.", "fatal")
        delTemp()
        return "error.laterPath"