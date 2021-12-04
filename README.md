SkinModPy 
===
## Info
SkinModPy is a program you can use to easily add accessories, clothing, and more to your skin.

So, for example, you can give your skin a chrismas hat.

Its main use is for events like christmas, to give your skin a cool christmas vibe.

*Note: Some subjects in this README are only valid on newer versions on SkinModPy, so be aware of that.*

## Installation
You can either install the executable from the releases tab, or install the source and run it with the python interpreter.

### Downloading From Releases
If you are on windows, you are able to download from a release. 

However, if you use Linux or macOS, you will need to compile from source.

### Running From Source
**You will need**
* [Python 3.9](https://www.python.org/) *or later*
* [Git](https://git-scm.com/)

**How To**
You will need to execute these commands in order to successfully clone the repository.
```bash
git clone https://github.com/talwat/SkinModPy
cd SkinModPy
```
Then, you will need to install the dependencies.

`pip install -r requirements.txt`

Finally, to run the program, do:

* **MAC & LINUX** `python src/main.py`

* **WINDOWS** `py src/main.py`

Or, if you want to build it as a binary, you can run the apropriate script in the `scripts` folder.

## Contribution
I dont really want code contributions due to how small this program is.

However, if you want to add a built in overlay, you can either
* Message me on discord `Talwat#2277` with the png of the overlay you would like to add.
* Make a pull request in the [SkinModPy-Database](https://github.com/talwhat/SkinModPy-Database) github repository.

I will make a guide to making a custom overlay eventually.

## Overlay info
Every overlay used with SkinModPy will have the color #FD00FE removed from the final output, so keep that in mind.

All overlays are stored [here](https://github.com/talwhat/SkinModPy-Database), so you can open a pull request to add overlays or download the ones you like individually for offline use.

## Why a GUI?
The program has a GUI to make it easier and faster to use, however if the os you use has issues with PySimpleGUI or its dependencies, you can modify the code to skip the GUI and go straight to overlaying.

You can edit `main.py`, and instead of the last line to be `overlay.main(<overlay>, <skin>)` instead of `ui.main()` and it will work!