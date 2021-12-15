import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TRANSPARENT_BUTTON
import overlay
import version
import github


def main():
    layout1 = [
        [sg.Text('Overlay Name'), sg.Combo(key="overlayInputName", values=github.fileNames, size=(45, 10), visible=True), sg.Button(button_color=TRANSPARENT_BUTTON, border_width=0)], 
    ]
    layout2 = [
        [sg.Text('Overlay Path'), sg.InputText(key="overlayInputPath"), sg.FileBrowse()],
    ]

    layout = [
        [sg.Text('Skin Path/Username'), sg.InputText(key="skinInput"), sg.FileBrowse()],
        [sg.Text()],
        [
            sg.Radio('Name', "overlayRadio", key="overlayRadio1", default=True, enable_events=True), 
            sg.Radio('Path', "overlayRadio", key="overlayRadio2", default=False, enable_events=True),
        ],
        [
            sg.Column(layout1, visible=True, key='overlayPath'),
            sg.Column(layout2, visible=False, key='overlayName')
        ],
        [sg.Text()],
        [sg.Text('Output:')],
        [sg.Output(size=(88, 20), key="output")],
        [sg.Button('Overlay!')],
    ]

    latestVersion = version.versionGet()
    if latestVersion != version.version:
        latestVersion = latestVersion.lower()
        if not(latestVersion.endswith("beta") or latestVersion.endswith("alpha") or latestVersion.endswith("dev")):
            layout.insert(0, [sg.Text("The latest version of SkinModPy is {}, but you are on {}!".format(latestVersion, version.version), text_color="#ffa500")])
    window = sg.Window('SkinModPy ' + version.version, layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'Cancel', 'Quit'):
            break
        if "overlayRadio1" in event:
            window['overlayName'].update(visible=False)
            window['overlayPath'].update(visible=True)
        if "overlayRadio2" in event:
            window['overlayPath'].update(visible=False)
            window['overlayName'].update(visible=True)
        if event == 'Overlay!':
            window['output'].Update('')
            if values["overlayRadio1"] == True:
                overlay.main(values["overlayInputName"], values["skinInput"])
            elif values["overlayRadio2"] == True:
                overlay.main(values["overlayInputPath"], values["skinInput"])