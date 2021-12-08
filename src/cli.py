import version
import overlay

print("SkinModPy {} (CLI MODE)\n".format(version.version))
overlayInput = input("What is the name/file path of the overlay you would like: ")
skinInput = input("What is the username/file path of the skin you would like: ")
overlay.main(overlayInput, skinInput)
input("Press enter to exit.")