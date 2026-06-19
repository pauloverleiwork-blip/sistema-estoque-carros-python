
def validacao_int(msg):
    while True:
        try:
            valor = int(input(msg).strip())
            if valor < 0:
                print('Valores negativos são inválidos!')
                continue
            return valor
        except ValueError:
            print('Insira somentes números!')

def mostrar_carros(carros):

    if not carros:
        print('\nNenhum carro encontrado!')
        return

    for i, carro in enumerate(carros, start = 1):
        print(
            f'\n{i} - {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')

