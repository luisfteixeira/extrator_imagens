import os
import requests
import csv
import time
import os.path

link_url = []

print('----------------------------------------------')
print(' BETHA SISTEMAS - FILIAL SANTA CRUZ DO SUL/RS ')
print('----------------------------------------------')
print('')

if(os.path.isfile('arquivo.csv')):
    print('#### INICIANDO EXTRAÇÃO DAS FOTOS!!! ####')
    print('')

    OUTPUT_DIR = './FOTOS'
    if os.path.isdir(OUTPUT_DIR) == True:
        print('>>>> Diretório /FOTOS já existe!!! <<<<')
        print('')
    else:
            os.mkdir(OUTPUT_DIR)
            print('#### Criando diretório /FOTOS!!! ####')
            print('')

    with open('arquivo.csv', 'r') as arq:
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
                        if resposta.status_code == requests.codes.OK:
                            with open(endereco, 'wb') as novo_arquivo:
                                novo_arquivo.write(resposta.content)
                            print("Download concluido!. Arquivo nome: {}".format(nome_imagem) +" / Estabelecimento: {}".format(nome_estab))
                            
                        else:
                            print("Link Expirado!. Gerar o arquivo novamente!")

                    if resposta.status_code == 200:
                        BASE_URL = link_url
                        OUTPUT_DIR = './FOTOS'

                        for i in range(1, 2):
                            nome_arquivo = os.path.join(OUTPUT_DIR, '{}.jpg'.format(nome_imagem))
                            baixar_arquivo(BASE_URL, nome_arquivo)
                    elif resposta.status_code != 200:
                        print("Link Expirado!. Gerar o arquivo novamente!")
                        break
else:
    print("******* Não foi possivel localizar o arquivo.csv !!! *******")
    print('')
    print("**** SALVE O ARQUIVO NO MESMO DIRETÓRIO DO EXTRATOR !!! ****")
        
time.sleep(10)