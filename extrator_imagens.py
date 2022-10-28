from PySimpleGUI import PySimpleGUI as sg
import os, os.path
import requests
import csv
import time
import logging


logging.basicConfig(level=logging.INFO, filename="log_programa.log", format="%(asctime)s - %(levelname)s - %(message)s")
diretorio_csv = os.getcwd()
diretorio_save = os.getcwd()

sg.theme('Material1')
layout = [
    [sg.Image(filename="favicon-16x16.png"), sg.Text('BETHA SISTEMAS LTDA.')],
    [sg.Text('Selecione o arquivo ".csv":')], 
    [sg.InputText(key='-FILE_PATH-'), 
    sg.FileBrowse(initial_folder =diretorio_csv, file_types = [("CSV Files", "*.csv")])],
    [sg.Text('Selecione o local da pasta:')],
    [sg.InputText(key='folder'), 
     sg.FolderBrowse()],
    [sg.Button('Iniciar Extração'), sg.Button('Cancelar') ,sg.Button('Sair')],
    [sg.Output(size=(70, 8))],
    [sg.Text('Extrator de Imagens - Versão 2.0')],
    [sg.Text('Filial Santa Cruz do Sul/RS - 2022')]
    
]
window = sg.Window("Extrator de Imagens - Betha Sistemas Ltda.", layout)
link_url = []


while True:
    event, values = window.read()
    
    cancelar = 'false'
    if event == 'Cancelar': 
        cancelar = 'true';
    else:
        if event == 'Iniciar Extração' and values['-FILE_PATH-'] and values['folder']:

            
            if(os.path.isfile(values['-FILE_PATH-'])):
                print('#### INICIANDO EXTRAÇÃO DAS FOTOS!!! ####')
                print('')
                logging.info('------------------------------------------')
                logging.info('#### INICIANDO EXTRAÇÃO DAS FOTOS!!! ####')
                logging.info('')


                OUTPUT_DIR = values['folder'] + '/FOTOS'
                if os.path.isdir(OUTPUT_DIR) == True:
                    print('>>>> Diretório /FOTOS já existe!!! <<<<')
                    print('')
                    logging.info('>>>> Diretório /FOTOS já existe!!! <<<<')
                    logging.info('')

                else:
                    directory = "FOTOS"
                    parent_dir = values['folder']
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)
                    print('#### Criando diretório /FOTOS!!! ####')
                    print('')
                    logging.info('#### Criando diretório /FOTOS!!! ####')
                    logging.info('')

                with open(values['-FILE_PATH-'], 'r') as arq:
                        leitor = csv.reader(arq, delimiter=';')
                        linhas = 0
                        

                        next(leitor)
                        for coluna in leitor:
                            if linhas == 1:
                                linhas += 1

                            elif coluna[9] != "":
                                
                                link_url = str(coluna[9])
                                nome_imagem = str(coluna[8])
                                linhas +=1

                                link_url = link_url
                                nome_imagem = str(coluna[8])
                                nome_estab = str(coluna[6])
                                resposta = requests.get(link_url)
                                def baixar_arquivo(url, endereco):
                                # faz requisição ao servidor
                                    resposta = requests.get(link_url)
                                    if resposta.status_code == requests.codes.OK and cancelar == 'false':
                                        with open(endereco, 'wb') as novo_arquivo:
                                            novo_arquivo.write(resposta.content)
                                        #window.read()
                                        print("Foto nome: {}".format(nome_imagem) +" /{}".format(nome_estab))
                                        logging.info("Foto nome: {}".format(nome_imagem) +" /{}".format(nome_estab))
                                        window.refresh()
                                    for i in nome_imagem:
                                        time.sleep(0.0000000001)

                                    else:
                                        print("Download concluído com sucesso!")
                                        logging.info("Download concluído com sucesso!")

                                if resposta.status_code == 200:
                                    BASE_URL = link_url
                                    #OUTPUT_DIR = './FOTOS'

                                    for i in range(1, 2):
                                        nome_arquivo = os.path.join(OUTPUT_DIR, '{}.jpg'.format(nome_imagem))
                                        baixar_arquivo(BASE_URL, nome_arquivo)
                                elif resposta.status_code != 200:
                                    print("Link Expirado!. Gerar o arquivo novamente!")
                                    logging.error("Link Expirado!. Gerar o arquivo novamente!")
                                    
                                    break
            else:
                print("******* Não foi possivel localizar o arquivo.csv !!! *******")
                print('')
                print("**** SALVE O ARQUIVO NO MESMO DIRETÓRIO DO EXTRATOR !!! ****")
                logging.error("******* Não foi possivel localizar o arquivo.csv !!! *******")
                logging.error('')
                logging.error("**** SALVE O ARQUIVO NO MESMO DIRETÓRIO DO EXTRATOR !!! ****")
            
    if event in (sg.WIN_CLOSED, 'Sair'):
        break

window.close()

#time.sleep(10)