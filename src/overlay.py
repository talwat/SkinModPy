import os

from PIL import Image 
import mojang
import methods
import overlayDownload

def main(overlayInput, input):
    if("/" in input or "." in input):
        name = False
    else:
        name = True

    if not os.path.isdir("overlays"):
        methods.log("Overlays directory not found.", "error")
        overlayDownload.main()
    overlayInputParsed = "overlays/{}.png".format(methods.parse(overlayInput))
    if(os.path.isfile(overlayInputParsed)):
        overlay = Image.open(overlayInputParsed)
    else:
        methods.log("Overlay not found.", "fatal")
        return "error.overlay"
    if(name):
        methods.log("Downloading skin...")
        if not(mojang.getSkin(input, "downloadedSkin.png") == "success"):
            methods.log("User not found.", "fatal")
            return "error.skinGet"
        else:
            methods.log("Loading skin...")
            skin = Image.open("downloadedSkin.png")
    else:
        if os.path.isfile(input):
            methods.log("Loading skin...")
            skin = Image.open(input)
        else:
            methods.log("The file couldn't be found.", "fatal")
            return "error.path"
    
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
    methods.log("Done!", "success")
    return "success"