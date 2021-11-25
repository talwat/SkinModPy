import os 
import mojang
import methods

def init():
    if not os.path.isdir("overlays"):
        print("Overlays directory not found, making directory...")
        if(os.path.isfile("overlays.zip")):
            os.remove("overlays.zip")
        methods.downloadFile("https://www.dropbox.com/s/rcdlkp9nexzn5du/overlays.zip?dl=1", "overlays.zip")
        methods.unzip("overlays.zip", "overlays")
        os.remove("overlays.zip")

def main():
    def delTemp():
        if os.path.isdir("temp"):
            from shutil import rmtree
            rmtree("temp")

    init()
    invalidOverlay = True
    while invalidOverlay:
        answer = methods.parse(input("What overlay do you want? "))
        if(os.path.isfile("overlays/{}.png".format(answer))):
            overlayPath = answer
            invalidOverlay = False
        else:
            print(answer + " does not exist.")
    nameOrFile = methods.getInput("Would you like to get a skin from a name, or a file? (n/f) ", ["n", "name", "f", "file"])
    path = ""
    if(nameOrFile == "n" or nameOrFile == "name"):
        if not os.path.isdir("temp"):
            os.mkdir("temp")
        invalidName = True
        while invalidName:
            answer = input("What is the name of the player with the skin you would like? ")
            if(mojang.getSkin(answer, "temp/skin.png") == "success"):
                print("{}'s skin has been successfully downloaded!".format(answer))
                path = "temp/skin.png"
                invalidName = False
            else:
                print("{} could not be found.".format(answer))
    else:
        invalidPath = True
        while invalidPath:
            answer = input("What is the path of the skin you want? ")
            if os.path.isfile(answer):
                path = answer
                invalidPath = False
            else:
                print("Invalid path.")
    
    if os.path.isfile(path):
        print("Overlaying Image...")
        methods.overlayImage(path, "overlays/{}.png".format(overlayPath), "output.png")
        print("Image overlayed!")
        delTemp()
        print("Done!")
    else:
        print("Path is invalid")
        delTemp()
        return