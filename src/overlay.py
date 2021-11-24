from PIL import Image
import urllib.request
import os 
import mojang

def unzip(zipFilePath, pathToExtract):
    import zipfile
    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        zip_ref.extractall(pathToExtract)

def overlayImage(skinPath, overlayPath, outputPath):
    img = Image.open(skinPath)
    overlay = Image.open(overlayPath)
    img.paste(overlay, (0, 0), overlay)
    img.save(outputPath, "PNG")

def parseSearch(input):
    result = ""
    result = input
    result = result.lower()
    result = result.replace(" ", "")
    return result

def downloadFile(url, path):
    urllib.request.urlretrieve(url, path)

def init():
    if not os.path.isdir("overlays"):
        print("Overlays directory not found, making directory...")
        downloadFile("https://www.dropbox.com/s/rcdlkp9nexzn5du/overlays.zip?dl=1", "overlays.zip")
        unzip("overlays.zip", "overlays")
        os.remove("overlays.zip")

def main():
    init()
    overlayPath = parseSearch(input("What overlay do you want? "))
    nameOrFile = input("Would you like to get a skin from a name, or a file? ").lower()
    if(nameOrFile == "n" or nameOrFile == "name"):
        if not os.path.isdir("temp"):
            os.mkdir("temp")
            name = input("What is the name of the player with the skin you would like? ")
            if(mojang.getSkin(name, "temp/skin.png") == "success"):
                print("{}'s skin has been successfully downloaded!".format(name))
                overlayImage("temp/skin.png", "")
            else:
                print("{} could not be found.".format(name))
                return