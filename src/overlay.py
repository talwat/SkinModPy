import methods
import overlayDownloads

def main(overlayInput, input):
    try:
        skin = overlayDownloads.skin(methods.filePath(input), input)
        if("error" in str(skin)):
            return
        overlay = overlayDownloads.overlay(methods.filePath(overlayInput), overlayInput)
        if("error" in str(overlay)):
            return
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
        methods.safelyRemoveFile("downloadedSkin.png", "Deleting downloaded skin from the Mojang API...")
        methods.safelyRemoveFile("downloadedOverlay.png", "Deleting downloaded overlay from the SkinModPy database...")
        methods.log("Done!", "success")
        return "success"
    except Exception as e:
        methods.log("An error occured: {}.".format(str(e)), "fatal")
        return "error"