
def validacao_int(msg):
    while True:
        try:
            valor = int(input(msg).strip())
            if valor < 0:
                print('Valores negativos são inválidos!')
                continue
            return valor
        except ValueError:
            print('Insira somente números!')

def validacao_texto(msg):
    while True:
        texto = input(msg).upper().strip()

        if texto == '':
            print('O campo não pode ficar vazio!')
            continue
        return texto

def mostrar_carros(carros):

    if not carros:
        print('\nNenhum véiculo cadastrado!')
        return

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