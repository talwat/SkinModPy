import overlay
import overlayDownload
import os
from methods import getInput

def consoleClear():
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")

consoleClear()
print("SkinModPy 1.0\n")

inputVar = getInput(
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