from requests import get
from os import system

system('cls')
def Converter():
    moedaExiste = False
    system('cls')
    print(f'                CONVERTER MOEDA\n\n')
    while True:
        try:
            moedaOrigem = str(input('Digite a moeda de origem: ')).upper()
            valor = float(input(f'Digite o valor em {moedaOrigem}: '))
            moedaDestino = str(input('Digite a moeda de destino: ')).upper()
            moeda = f'{moedaOrigem}-{moedaDestino}'
            request = get(f"https://economia.awesomeapi.com.br/last/{moeda}").json()
            try:
                verificacao = request['code']
            except:
                moedaExiste = True
        except:
            print('ERRO! Tente novamente.')
            input('Pressione ENTER para continuar...')
            system('cls')
        finally:
            if moedaExiste is False:
                print('ERRO! Moeda inválida ou inexistente.')
                input('Pressione ENTER para continuar...')
                system('cls')
            else:
                break

    coinInfo = request[f'{moedaOrigem}{moedaDestino}']
    valorConvertido = valor * float(coinInfo['high'])
    print(f'''Horário da cotação: {coinInfo["create_date"]}
Conversão de {valor} {coinInfo["code"]} para {coinInfo["codein"]} ({coinInfo["name"]})
\nO valor convertido é: {valorConvertido}''')
    input('\nPressione ENTER para continuar...')
    system('cls')

def ListaMoedas():
    system('cls')
    print(f'                LISTAR MOEDAS\n\n')
    request = get('https://economia.awesomeapi.com.br/json/all').json()
    moedas = ['USD', 'USDT', 'CAD', 'GBP', 'ARS', 'BTC', 'LTC', 'EUR', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'ETH', 'XRP', 'DOGE']
    print(f'{"MOEDA ORIGEM":<10}{"MOEDA FINAL":^10}{"NOME":^20}{"COTAÇÃO":>58}{"DATA":>55}')
    for c in range(0, len(moedas)):
        code, codein, name, cotacao, data = request[moedas[c]]['code'] , request[moedas[c]]['codein'], request[moedas[c]]['name'], request[moedas[c]]['high'], request[moedas[c]]['create_date']
        print(f'{code:<10}{codein:^20}{name:^40}{cotacao:>35}{data:>45}')
    input('\nPressione ENTER para continuar...')
    system('cls')

while True:
    print('''               CONVERSOR DE MOEDAS
[ 1 ] - Converter moeda
[ 2 ] - Lista de moedas disponíveis
[ 3 ] - Sair''')
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Opção inválida! Tente Novamente.')
        continue
    else:
        if opcao == 1:
            Converter()
        elif opcao == 2:
            ListaMoedas()
        elif opcao == 3:
            print('Saindo...')
            break
            exit()
        else:
            print('Opção inválida!')
            continue