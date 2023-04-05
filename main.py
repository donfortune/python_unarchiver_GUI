import PySimpleGUI as sg
from  zip_extract import unzip_archive

sg.theme('Black')
label1 = sg.Text('Add zip file')
input1 = sg.Input()
button1 = sg.FileBrowse("Select", key='zip')

label2 = sg.Text('Select destination folder')
input2 = sg.Input()
button2 = sg.FolderBrowse('choose', key='folder')

button3 = sg.Button('Unzip')
output = sg.Text(key='output')

window = sg.Window("Zip Extractor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [button3, output]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    file_path = values['zip']
    dest = values['folder']
    unzip_archive(file_path, dest)
    window['output'].update(value='UNZIPPED SUCCESSFULLY')

window.close()
