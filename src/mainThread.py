import ui
import version
import sys
import overlay

args = sys.argv
print("SkinModPy {}\n".format(version.version))

if(".py" in args[0]):
    args.pop(0)

if(len(args) <= 1):
    ui.main()
else:
    overlay.main(args[0], args[1])