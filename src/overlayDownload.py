import os
import methods
from shutil import rmtree

def main():
    try:
        if os.path.isdir("overlays"):
            methods.log("Old overlays directory found, deleting...")
            rmtree("overlays")
        if(os.path.isfile("overlays.zip")):
            os.remove("overlays.zip")
        methods.log("Downloading overlays...")
        methods.downloadFile("https://www.dropbox.com/s/rcdlkp9nexzn5du/overlays.zip?dl=1", "overlays.zip")
        methods.log("Unpacking overlays...")
        methods.unzip("overlays.zip", "overlays")
        methods.log("Removing left-over packed overlays...")
        os.remove("overlays.zip")
        methods.log("Done downloading overlays!", "success")
        return "success"
    except:
        methods.log("A fatal error occured.", "fatal")
        return "error"
