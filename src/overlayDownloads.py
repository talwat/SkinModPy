from mojang import getSkin
import methods
from database import getOverlay
from PIL import Image
import os

def overlay(database, input):
    if(database):
        inputParsed = "overlays/{}.png".format(methods.parse(input))
        methods.log("Downloading overlay...")
        overlayResponse = getOverlay(inputParsed)
        if(overlayResponse == "success"):
            methods.log("Loading overlay...")
            overlay = Image.open("downloadedOverlay.png")
            return overlay
        elif(overlayResponse == "404"):
            methods.log("Overlay not found.", "fatal")
            return "error.overlay404"
        else:
            return "error.overlay"
    else:
        if os.path.isfile(input):
            methods.log("Loading overlay...")
            overlay = Image.open(input)
            return overlay
        else:
            methods.log("The overlay file couldn't be found.", "fatal")
            return "error.overlayPath"
def skin(name, input):
    if(name):
        skinResponse = getSkin(input, "downloadedSkin.png")
        if(skinResponse == "success"):
            methods.log("Loading skin...")
            skin = Image.open("downloadedSkin.png")
            return skin
        elif(skinResponse == "404"):
            methods.log("Skin not found", "fatal")
            return "error.skin404"
        else:
            return "error.skin"
    else:
        if os.path.isfile(input):
            methods.log("Loading skin...")
            skin = Image.open(input)
            return skin
        else:
            methods.log("The skin file couldn't be found.", "fatal")
            return "error.skinPath"