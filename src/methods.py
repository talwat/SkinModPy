import urllib.request
import base64

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

def getInput(prompt, validInputs):
    keepAsking = True
    while keepAsking:
        answer = parse(input(prompt))
        for validInput in validInputs:
            if answer == validInput:
                keepAsking = False;
                return answer
        print("Invalid Input")

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