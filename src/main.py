import overlay
import overlayDownload
import os
from json import loads
import methods

version = "1.1"

def consoleClear():
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")

consoleClear()

try:
	programInfo = loads(methods.getFromInternet("https://raw.githubusercontent.com/talwat/SkinModPy/master/program.json"))
except:
	programInfo = {}

if(programInfo != {}):
    if programInfo["version"] != version:
       print("The latest version of SkinModPy is {}, but you are on {}!".format(programInfo["version"], version))
print("SkinModPy {}\n".format(version))

inputVar = methods.getInput(
    "Please enter what you would like to do:\n" +
    "0 - Exit the program\n" +
    "1 - Put an overlay on a skin\n" +
    "2 - Download all the overlays from dropbox\n",

    ["0", "1", "2"]
)
if(inputVar == "0"):
    quit()
elif(inputVar == "1"):
    overlay.main()
elif(inputVar == "2"):
    overlayDownload.main()