from PIL import Image
import urllib.request

def overlayImage(path0, path1, outputPath):
    img = Image.open(path0)
    overlay = Image.open(path1)
    img.paste(overlay, (0, 0), overlay)
    img.save(outputPath, "PNG")

def init():
    import os 
    if not os.path.isdir("overlays"):
        print("Overlays directory not found, making directory...")
        downloadFile("PLACEHOLDERS", "overlays.zip")

def main():
    init()
    overlayImage("test/skin.png", "test/overlay.png", "test/output.png")

def downloadFile(url, path):
    urllib.request.urlretrieve(url, path)