import requests
import datetime

dicionario = {}
def cotacoes_dolar():
    # pegar as cotações da API.
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    # transformar em json
    cotacao = cotacao.json()
    # transformar em float. informação está em str
    dolar = float(cotacao['USDBRL']['bid'])
    euro = float(cotacao['EURBRL']['bid'])
    # data atual
    data_atual = datetime.datetime.now()
    print(cotacao)
    # ctime() reorganiza a formatação da data
    print(f'Em {data_atual.ctime()}, o valor do dólar é: ${dolar:.2f}')
    # \N, consigo colocar o sinal do euro
    print(f'Em {data_atual.ctime()}, o valor do Euro é: \N{euro sign}{euro:.2f}')
    # atualizando o dicionário
    dicionario.update({'dolar':dolar})
    dicionario.update({'euro': euro})
    print(dicionario)
    dolar_str = str(dolar)
    euro_str = str(euro)
    with open("cotacao.txt", "a") as cotacao:
        cotacao.write(dolar_str)

cotacoes_dolar()
