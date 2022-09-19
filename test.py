# Projeto cotação dólar e criar um arquivo.txt

import requests
import datetime

def dolar():
    # pegar cotação da API
    cotacao = requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    # transformar em json
    cotacao = cotacao.json()
    print(cotacao)
    # extrair somente o valor do dólar.
    valor_dolar = float(cotacao['USDBRL']['bid'])
    valor_euro = float(cotacao['EURBRL']['bid'])
    print(valor_dolar, valor_euro)
    # data atual
    data_atual = datetime.date.today()
    print(f'Em {data_atual.day}/{data_atual.month}/{data_atual.year}, o valor do dólar é: ${valor_dolar:.2f}')
    print(f'Em {data_atual.day}/{data_atual.month}/{data_atual.year}, o valor do euro é: \N{euro sign}{valor_euro:.2f}')
    dolar_str = str(valor_dolar)
    dia_str = str(data_atual.day)
    mes_str = str(data_atual.month)
    ano_str = str(data_atual.year)
    frase = 'Em '+dia_str+'/'+mes_str+'/'+ano_str+', o valor do dólar é: $'+dolar_str+'\n'
    print(frase)

    #começar a criar o arquivo.txt
    with open('cotacao.txt', 'a') as arquivo:
        arquivo.write(frase)

        arquivo.close()
dolar()