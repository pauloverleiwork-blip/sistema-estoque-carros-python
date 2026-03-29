import json

#===Constantes===
ARQUIVO_DADOS = 'carros.json'

#===Funções de Persistencia===
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8' ) as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados():
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(carros, arquivo, indent=2, ensure_ascii=False)

#===Dados Globais===
carros = carregar_dados()

modulos = ['marca','modelo','ano','cor',]
marcas = []

#===Atualiza a lista de marcas===
for carro in carros:
    marca = carro['marca']
    if marca not in marcas:
        marcas.append(marca)

#====Funções de Sistema====
def menu_principal():
    while True:
        print('\n====Estoque de Veículos====\n1 - Adicionar\n2 - Deletar\n3 - Listar\n4 - Filtrar\n5 - Alterar preço\n0 - Sair')
        op = input('Digite: ').strip()
        if op == '1':
            adicionar_carro()
        elif op == '2':
            deletar_carro()
        elif op == '3':
            listar_carros()
        elif op == '4':
            filtrar_carros()
        elif op == '5':
            alterar_preco()
        elif op == '0':
            break
        else:
            print('\nDigite uma opção válida!')

def adicionar_carro():

    novo_carro = {}

    for modulo in modulos:

        valor = input(f'Digite {modulo}: ').strip().upper()
        novo_carro[modulo] = valor

    while True:
        preco = input('Digite o preço: ')
        if not preco.isdigit():
            print('Opção inválida')
        else:
            break

    while True:
        quilometragem = input('Digite a Quilometragem: ')
        if not quilometragem.isdigit():
            print('Opção inválida')
        else:
            break

    quilometragem = int(quilometragem)

    novo_carro['preco'] = preco
    novo_carro['quilometragem'] = quilometragem


    carros.append(novo_carro)
    salvar_dados()

    if novo_carro['marca'] not in marcas:
        marcas.append(novo_carro['marca'])

def deletar_carro():
    while True:
        if not carros:
            print('\nNenhum carro para deletar!')
            break

        for i, carro in enumerate(carros, start=1):
            print(f'\n{i} - {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')

        print('0 - Voltar')

        op = input('Digite: ').strip()

        if op == '0':
            break

        if not op.isdigit():
            print('Opção inválida')
            continue

        op = int(op)

        if 1 <= op <= len(carros):
            carro_removido = carros.pop(op -1)
            print('Operação realizada com sucesso!')

            marca_removida = carro_removido['marca']
            if not any(carro['marca'] == marca_removida for carro in carros):
                marcas.remove(marca_removida)

            salvar_dados()
        else:
            print('Opção inválida!')

def listar_carros():
    if not carros:
        print('\nNunhum carro cadastrado!')
        return

    for carro in carros:
        print(f'\nMarca: {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')

    input('\nPressione Enter para voltar.')
def filtrar_carros():
    while True:
        print('\n1 - Filtrar por marca\n2 - Filtrar por preço\n0 - Voltar')
        op = input('Digite: ').strip()

        if op == '1':
            filtrar_marca()
        elif op == '2':
            filtrar_preco()
        elif op == '0':
            break
        else:
            print('Digite uma opção válida!')

def filtrar_marca():
    while True:
        if not marcas:
            print('\nNenhuma marca encontrada!')
            break

        for i, marca in enumerate(marcas, start = 1):
           print(f'{i} - {marca}')

        print('0 - Voltar')

        op = input('Digite: ').strip()

        if op == '0':
                break

        if not op.isdigit():
                print('Opção inválida')
                continue

        op = int(op)

        if 1 <= op <= len(marcas):
            for carro in carros:
                if carro['marca'] == marcas[op -1]:
                    print(f"\nMarca: {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}")
            input('Pressione Enter para continuar')
        else:
            print('Opção inválida')

def filtrar_preco():
    while True:
        while True:
            minimo = input('Valor minimo: ').strip()

            if not minimo.isdigit():
                print('Opção inválida')
            else:
                break

        while True:
            maximo = input('Digite o valor máximo: ').strip()

            if not maximo.isdigit():
                print('Opção inválida')
            else:
                break

        minimo = int(minimo)
        maximo = int(maximo)

        encontrou = False
        for carro in carros:
            if minimo <= carro['preco'] <= maximo:
                encontrou = True
                print(f'\nMarca: {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')

        if not encontrou:
          print('\nNenhum carro encontrado nessa faixa de preço!')

        input('\nPressione Enter para voltar.')
        break

def alterar_preco():
    while True:
        if not carros:
            print('\nNenhum veículo cadastrado!')
            break

        for i,carro in enumerate(carros, start=1):
            print(f'\n{i} - {carro['marca']}\nModelo: {carro['modelo']}\nCor: {carro['cor']}\nQuilometragem: {carro['quilometragem']:,}\nAno: {carro['ano']}\nPreço: R${carro['preco']:,}')
        print('\n0 - Voltar')

        op = input('Digite o carro que desejada alterar o preço: ').strip()

        if op == '0':
            break

        if not op.isdigit():
            print('Opção inválida')
            continue

        op = int(op)

        if 1 <= op<= len(carros):
            carro_selecionado = carros[op-1]
            while True:
                print(f'\nValor atual: R${carro_selecionado['preco']:,}')
                print('0 - Voltar.')

                valor = input('Digite o novo valor: R$').strip()

                if valor == '0':
                    break

                if not valor.isdigit():
                    print('Opção inválida')
                    continue

                valor = int(valor)

                carro_selecionado['preco'] = valor
                print('Alteração realizada!')
                salvar_dados()
                break
        else:
            print('Opção inválida')

menu_principal()
