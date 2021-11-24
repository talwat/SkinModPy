import overlay
import overlayDownload
import os

def consoleClear():
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")

consoleClear()
print("SkinModPy 1.0\n")

invalidInput = True
while invalidInput:
    inputVar = input(
        "Please enter what you would like to do:\n" +
        "0 - Exit the program\n" +
        "1 - Put an overlay on a skin\n" +
        "2 - Download all the overlays from a google drive link.\n"
    )
    match inputVar:
        case "0":
            quit()
        case "1":
            overlay.main()
            invalidInput = False;
        case "2":
            overlayDownload.main()
            invalidInput = False;
        case _:
            consoleClear()
            print("Invalid Input")