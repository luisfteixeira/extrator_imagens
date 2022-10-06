from PySimpleGUI import PySimpleGUI as sg
import csv, os

diretorio_inicial = os.getcwd()
csv_path = str()

# Layout
sg.theme('Material1')
layout = [
    [sg.Text('Selecione o arquivo ".csv":')], 
    [sg.InputText(key='-FILE_PATH-'), 
    sg.FileBrowse(initial_folder =diretorio_inicial, file_types = [("CSV Files", "*.csv")])],
    [sg.Text('Selecione o local da pasta:')], 
    [sg.Input(key='pasta', size=(20, 1))],
    #[sg.]
    [sg.Button('Iniciar Extração'), sg.Button('Sair')],
]

window = sg.Window("Extrator de Imagens - Betha Sistemas Ltda.", layout)


def convert_csv_array(csv_address):
    file = open(csv_address)
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)
    file.close()
    return rows

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
    elif event == "Iniciar Extração":
        csv_address = values["-FILE_PATH-"]
        print(convert_csv_array(csv_address))   
window.close()
