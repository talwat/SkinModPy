import os

from PIL import Image 
from mojang import getSkin
import methods
from database import getOverlay

def main(overlayInput, input):
    if("/" in input or "." in input):
        name = False
    else:
        name = True
    
    if("/" in overlayInput or "." in overlayInput):
        database = False
    else:
        database = True

    if(database):
        overlayInputParsed = "overlays/{}.png".format(methods.parse(overlayInput))
        methods.log("Downloading overlay...")
        overlayResponse = getOverlay(overlayInputParsed)
        if(overlayResponse == "success"):
            methods.log("Loading overlay...")
            overlay = Image.open("downloadedOverlay.png")
        elif(overlayResponse == "404"):
            methods.log("Overlay not found", "fatal")
            return "error.overlay404"
        else:
            methods.log("An error occured while downloading the overlay.", "fatal")
            return "error.overlay"
    else:
        if os.path.isfile(overlayInput):
            methods.log("Loading overlay...")
            overlay = Image.open(overlayInput)
        else:
            methods.log("The overlay file couldn't be found.", "fatal")
            return "error.overlayPath"

    if(name):
        methods.log("Downloading skin...")
        skinResponse = getSkin(input, "downloadedSkin.png")
        if(skinResponse == "success"):
            methods.log("Loading skin...")
            skin = Image.open("downloadedSkin.png")
        elif(skinResponse == "404"):
            methods.log("Skin not found", "fatal")
            return "error.skin404"
        else:
            methods.log("An error occured while downloading the skin.", "fatal")
            return "error.skin"
    else:
        if os.path.isfile(input):
            methods.log("Loading skin...")
            skin = Image.open(input)
        else:
            methods.log("The skin file couldn't be found.", "fatal")
            return "error.skinPath"
    
    methods.log("Overlaying images...");
    overlayedImage = methods.overlayImage(skin, overlay)
    methods.log("Removing hex color #FD00FE...")
    finalImage = methods.replacePixels((253, 0, 254), overlayedImage)
    methods.log("Saving output...")
    finalImage.save("output.png")
    methods.log("Closing images...")
    overlayedImage.close()
    skin.close()
    overlay.close()
    if(os.path.isfile("downloadedSkin.png")):
        methods.log("Deleting downloaded skin from the Mojang API...")
        os.remove("downloadedSkin.png")
    if(os.path.isfile("downloadedOverlay.png")):
        methods.log("Deleting downloaded overlay from the SkinModPy database...")
        os.remove("downloadedOverlay.png")
    methods.log("Done!", "success")
    return "success"