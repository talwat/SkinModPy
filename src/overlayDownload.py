import os
import methods
from shutil import rmtree

def main():
    if os.path.isdir("overlays"):
        print("Old overlays directory found, deleting...")
        rmtree("overlays")
    if(os.path.isfile("overlays.zip")):
        os.remove("overlays.zip")
    print("Downloading overlays zip folder from dropbox...")
    methods.downloadFile("https://www.dropbox.com/s/rcdlkp9nexzn5du/overlays.zip?dl=1", "overlays.zip")
    print("Downloaded overlays!\nUnzipping overlays zip folder...")
    methods.unzip("overlays.zip", "overlays")
    print("Unzipped overlays!\nRemoving unecessary zip folder...")
    os.remove("overlays.zip")
    print("Done removing zip folder!\nDone!")