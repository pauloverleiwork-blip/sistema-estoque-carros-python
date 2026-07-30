from datetime import date
from config import carros
import os

def validacao_int(msg):
    while True:
        try:
            valor = int(input(msg).strip())
            if valor < 0:
                print('\nValores negativos são inválidos!')
                continue
            return valor
        except ValueError:
            print('\nInsira somente números!')

def validacao_texto(msg):
    while True:
        texto = input(msg).upper().strip()

        if texto == '':
            print('\nO campo não pode ficar vazio!')
            continue
        return texto

def mostrar_carros(carros):

    for i, carro in enumerate(carros, start = 1):
        print(
            f'\n{i} - {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')

def confirmar_acao(msg):
    while True:
        resposta = input(msg).strip().upper()

        if resposta == 'S':
            return True
        elif resposta == 'N':
            return  False
        else:
            print('\nDigite apenas S ou N!')


def validacao_ano(msg):
    ano_maximo = date.today().year + 1
    ano_minimo = 1886

    while True:
        ano = validacao_int(msg)

        if ano < ano_minimo:
            print(f'O ano não pode ser menor que {ano_minimo}')
            continue

        if ano > ano_maximo:
            print(f'O ano não pode ser maior que {ano_maximo}')
            continue

        return ano

def verificar_veiculos():
    if not carros:
        print('\nNenhum veículo cadastrado!')
        input('\nPressione Enter para voltar.')
        return True


def mostrar_titulo(titulo):
    limpar_tela()
    print(f'\n======{titulo}======')
    return

def limpar_tela():
    os.system('cls' if os.name =='nt' else 'clear')