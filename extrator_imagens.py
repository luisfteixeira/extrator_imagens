import os
import requests
import csv

link_url = []

with open('alunos.csv', 'r') as arq:
    leitor = csv.reader(arq, delimiter=';')
    linhas = 0
    
    next(leitor)
    for coluna in leitor:
        if linhas == 1:
            linhas += 1
        elif coluna[8] != "":
            link_url = str(coluna[8])
            nome_imagem = str(coluna[5])
            linhas +=1
            resposta = requests.get(link_url)
            def baixar_arquivo(url, endereco):
            # faz requisição ao servidor
                resposta = requests.get(link_url)
                
                if resposta.status_code == requests.codes.OK:
                    with open(endereco, 'wb') as novo_arquivo:
                        novo_arquivo.write(resposta.content)
                    print("Download concluido!. Arquivo nome: {}".format(nome_imagem))
                    
                else:
                    print("Link Expirado!. Gerar o arquivo novamente!")

            if resposta.status_code == 200:
                BASE_URL = link_url
                for i in range(1, 2):
                    nome_arquivo = os.path.join('{}.jpg'.format(nome_imagem))
                    baixar_arquivo(BASE_URL, nome_arquivo)
            elif resposta.status_code != 200:
                print("Link Expirado!. Gerar o arquivo novamente!")
                
