#TODO: Make the code more polished and less 💩

import os

from PIL import Image 
import mojang
import methods
import overlayDownload

def main(overlayInput, nameOrFileInput, nameOrPathInput):
    if not os.path.isdir("overlays"):
        methods.log("Overlays directory not found.", "error")
        overlayDownload.main()
    overlayInputParsed = "overlays/{}.png".format(methods.parse(overlayInput))
    if(os.path.isfile(overlayInputParsed)):
        overlayPath = overlayInputParsed
    else:
        methods.log("Overlay not found.", "fatal")
        return "error.overlay"
    overlay = Image.open(overlayPath)
    nameOrFile = nameOrFileInput
    if(nameOrFile == "n" or nameOrFile == "name"):
        methods.log("Downloading skin...")
        if not(mojang.getSkin(nameOrPathInput, "downloadedSkin.png") == "success"):
            methods.log("User not found.", "fatal")
            return "error.skinGet"
        else:
            methods.log("Loading skin...")
            skin = Image.open("downloadedSkin.png")
    else:
        if os.path.isfile(nameOrPathInput):
            methods.log("Loading skin...")
            skin = Image.open(nameOrPathInput)
        else:
            methods.log("The file couldn't be found.", "fatal")
            return "error.path"
    
    methods.log("Overlaying images...");
    overlayedImage = methods.overlayImage("image", skin, overlay)
    methods.log("Removing hex color #FD00FE...")
    finalImage = methods.replacePixels((253, 0, 254), "image", overlayedImage)
    methods.log("Saving output...")
    finalImage.save("output.png")
    methods.log("Closing images...")
    overlayedImage.close()
    skin.close()
    overlay.close()
    if(os.path.isfile("downloadedSkin.png")):
        methods.log("Deleting downloaded skin from the Mojang API...")
    methods.log("Done!", "success")
    return "success"