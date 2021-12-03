import PySimpleGUI as sg
import overlay
import overlayDownload
import version

def main():
    layout = [
        [sg.Text('Skin Path/Username'), sg.InputText(), sg.FileBrowse()],
        [sg.Text('Overlay Name'), sg.InputText()],
        [sg.Text('\nOutput:')],
        [sg.Output(size=(88, 20), key="output")],
        [sg.Button('Overlay!'), sg.Button('Download Latest Overlays')]
    ]
    latestVersion = version.versionGet()
    if latestVersion != version.version:
        latestVersion = latestVersion.lower()
        if not(latestVersion.endswith("beta") or latestVersion.endswith("alpha") or latestVersion.endswith("dev")):
            layout.insert(0, [sg.Text("The latest version of SkinModPy is {}, but you are on {}!".format(latestVersion, version.version), text_color="#ffa500")])
    window = sg.Window('SkinModPy ' + version.version, layout)
    while True:                             # The Event Loop
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel', 'Quit'):
            break
        if event == 'Overlay!':
            window.FindElement('output').Update('')
            overlay.main(values[1], values[0])
        if event == 'Download Latest Overlays':
            overlayDownload.main()
