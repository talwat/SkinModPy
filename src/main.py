import ui
import version
import github
from methods import log

print("SkinModPy {}\n".format(version.version))
log("Initializing...")
github.init()
log("Done Initializing!", "success")
log("Launching GUI...")
ui.main()