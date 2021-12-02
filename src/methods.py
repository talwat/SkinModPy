import urllib.request
import base64
import os
from PIL import Image

logTypes = {
    "success": "[SUCCESS]: ",
    "info": "[INFO]: ",
    "warn": "[WARN]: ",
    "error": "[ERROR]: ",
    "fatal": "[FATAL]: "
}

def log(message, logType = "info"):
    print(logTypes[logType] + message)

def replacePixels(color, inputPath, outputPath):
    img = Image.open(inputPath)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if(
            item[0] == color[0]
            and item[1] == color[1]
            and item[2] == color[2]
        ):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(outputPath, "PNG")

def getFromInternet(url):
    result = ""
    file = urllib.request.urlopen(url)
    for line in file:
	    decoded_line = line.decode("utf-8")
	    result += decoded_line
    return result

def base64Decode(input):
    base64_bytes = input.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes

def downloadFile(url, path):
    urllib.request.urlretrieve(url, path)

def unzip(zipFilePath, pathToExtract):
    import zipfile
    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        zip_ref.extractall(pathToExtract)

def overlayImage(skinPath, overlayPath, outputPath):
    from PIL import Image
    img = Image.open(skinPath)
    overlay = Image.open(overlayPath)
    img.paste(overlay, (0, 0), overlay)
    img.save(outputPath, "PNG")

def parse(input):
    result = ""
    result = input
    result = result.lower()
    result = result.replace(" ", "")
    return result

def consoleClear():
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")