from config import carros, marcas, MODULOS
from dados import salvar_dados
from utils import validacao_int, validacao_texto, mostrar_carros, confirmar_acao

def adicionar_carro():

    novo_carro = {}

    for modulo in MODULOS:

        valor = validacao_texto(f'Digite {modulo}: ')
        novo_carro[modulo] = valor

    preco = validacao_int('Digite o preço: R$ ')
    quilometragem = validacao_int('Digite a quilometragem: ')
    ano = validacao_int('Digite o ano: ')

    novo_carro['preco'] = preco
    novo_carro['quilometragem'] = quilometragem
    novo_carro['ano'] = ano

    carros.append(novo_carro)
    salvar_dados(carros)

    if novo_carro['marca'] not in marcas:
        marcas.append(novo_carro['marca'])

def deletar_carro():
    while True:
        if not carros:
            print('\nNenhum carro para deletar!')
            break

        mostrar_carros(carros)

        print('0 - Voltar')

        op = validacao_int('Digite: ')

        if op == 0:
            break

        if 1 <= op <= len(carros):

            carro_selecionado = carros[op - 1]

            print('\nVeículo selecionado:')
            mostrar_carros([carro_selecionado])
            if confirmar_acao("\nTem certeza que deseja deletar o veículo? [S/N]: "):
                carro_removido = carros.pop(op - 1)
                print('Operação realizada com sucesso!')

                marca_removida = carro_removido['marca']
                if not any(carro['marca'] == marca_removida for carro in carros):
                    marcas.remove(marca_removida)

                salvar_dados(carros)
            else:
                print('Operação cancelada!')
        else:
            print('Opção inválida')

def listar_carros():
    if not carros:
        print('\nNunhum carro cadastrado!')
        return

    mostrar_carros(carros)

    input('\nPressione Enter para voltar.')

def menu_filtrar_carros():
    while True:
        print('\n======FILTRAR======')
        print('\n1 - Marca\n2 - Preço\n3 - Quilometragem\n4 - Ano\n5 - Modelo\n6 - Cor\n0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            filtrar_marca()
        elif op == 2:
            filtrar_carro("Digite o valor mínimo: R$", "Digite o valor máximo: R$", "preco")
        elif op == 3:
            filtrar_carro("Digite a quilometragem mínima: ","Digite a quilometragem máxima: ", "quilometragem")
        elif op == 4:
            filtrar_carro('Digite o ano mínimo: ', 'Digite o ano máximo: ', 'ano')
        elif op == 5:
            buscar_carro('Digite o modelo desejado: ', 'modelo')
        elif op == 6:
            buscar_carro('Digite a cor desejada: ', 'cor')
        elif op == 0:
            break
        else:
            print('\nDigite uma opção válida!')

def filtrar_marca():
    while True:
        if not marcas:
            print('\nNenhuma marca encontrada!')
            break

        for i, marca in enumerate(marcas, start = 1):
           print(f'{i} - {marca}')

        print('0 - Voltar')

        op = validacao_int('\nDigite: ')

        if op == 0:
                break

        if 1 <= op <= len(marcas):
            marca_escolhida = marcas[op - 1]

            carros_filtrados = [
                carro for carro in carros
                if carro['marca'] == marca_escolhida
            ]

            mostrar_carros(carros_filtrados)
            input('\nPressione Enter para continuar')
        else:
            print('Opção inválida')

def buscar_carro(msg,campo):
    if not carros:
        print('Nenhum veículo encontrado!')
        return

    termo_busca = validacao_texto(msg)

    carros_filtrados = [
        carro for carro in carros
        if termo_busca in carro[campo].upper()
    ]

    mostrar_carros(carros_filtrados)
    input('\nPressione Enter para voltar.')

def filtrar_carro(msg_min,msg_max,modulo):
    while True:
        minimo = validacao_int(msg_min)

        maximo = validacao_int(msg_max)

        carros_filtrados = [
            carro for carro in carros
            if minimo <= carro[modulo] <= maximo
        ]

        mostrar_carros(carros_filtrados)

        input('\nPressione Enter para voltar.')
        break

def alterar_preco():
    while True:
        if not carros:
            print('\nNenhum veículo cadastrado!')
            break

        mostrar_carros(carros)

        print('\n0 - Voltar')

        op = validacao_int('\nDigite o carro que desejada alterar o preço: ')

        if op == 0:
            break

        if 1 <= op <= len(carros):
            carro_selecionado = carros[op - 1]
            while True:
                print(f'\nValor atual: R${carro_selecionado['preco']:,}')
                print('0 - Voltar.')

                valor = validacao_int('\nDigite o novo valor em R$: ')

                if valor == 0:
                    break

                carro_selecionado['preco'] = valor
                print('Alteração realizada!')
                salvar_dados(carros)
                break
        else:
            print('Opção inválida')