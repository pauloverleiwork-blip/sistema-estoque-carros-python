from time import process_time_ns

from config import carros, marcas, MODULOS
from dados import salvar_dados
from utils import validacao_int, validacao_texto, mostrar_carros, confirmar_acao

#=====ADICIONA VEICULOS AO ESTOQUE=====

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

#=====DELETA VEICULOS DO ESTOQUE=====

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

#=====LISTAS=====

#lista todos os veiculos do estoque
def listar_carros():
    if not carros:
        print('\nNunhum carro cadastrado!')
        return

    mostrar_carros(carros)

    input('\nPressione Enter para voltar.')

#Lista marcas disponiveis no estoque
def listar_marcas():
    if not marcas:
        print('\nNenhuma marca encontrada!')
        return

    print('\n======MARCAS DISPONÍVEIS======')

    for marca in marcas:
       print(f'- {marca}')

    input('\nPressione Enter para continuar.')

#=====MENU DE FILTRO DE VEICULOS=====

def menu_filtrar_carros():
    while True:
        print('\n======FILTRAR======')
        print('\n1 - Marca\n2 - Preço\n3 - Quilometragem\n4 - Ano\n5 - Modelo\n6 - Cor\n7 - Listar marcas disponíveis\n0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            buscar_carro('Digite a marca desejada: ', 'marca')
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
        elif op == 7:
            listar_marcas()
        elif op == 0:
            break
        else:
            print('\nDigite uma opção válida!')

#=====FILTROS DE VEICULOS=====#

#Filtra veiculos por cor, modelo e marca
def buscar_carro(msg, campo):
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

#filtra veiculos por minimo e maximo, ano, preço e quilometragem
def filtrar_carro(msg_min, msg_max, campo):
    while True:
        minimo = validacao_int(msg_min)

        maximo = validacao_int(msg_max)

        carros_filtrados = [
            carro for carro in carros
            if minimo <= carro[campo] <= maximo
        ]

        mostrar_carros(carros_filtrados)

        input('\nPressione Enter para voltar.')
        break

#=====MENU ORDENAR VEICULOS=====

def menu_ordenar_carros():
    while True:
        print('\n======ORDENAR VEÍCULOS======')
        print('\n1 - Preço: menor para maior')
        print('2 - Preço: maior para menor')
        print('3 - Ano: mais antigo para mais novo')
        print('4 - Ano: mais novo para mais antigo')
        print('5 - Quilometragem: menor para maior')
        print('6 - Quilometragem: maior para menor')
        print('0 - Voltar')

        op = validacao_int('\nDigite: ')

        if op == 1:
            ordenar_carros('preco', False)
        elif op == 2:
            ordenar_carros('preco', True)
        elif op == 3:
            ordenar_carros('ano', False)
        elif op == 4:
            ordenar_carros('ano', True)
        elif op == 5:
            ordenar_carros('quilometragem', False)
        elif op == 6:
            ordenar_carros('quilometragem', True)
        elif op == 0:
            break
        else:
            print('\nDigite uma opção válida!')

#Função de ordenação de veiculos

def ordenar_carros(campo, reverso):
    if not carros:
        print('\nNenhum veículo cadastrado!')
        return
    carros_ordenados = sorted(carros, key=lambda carro: int(carro[campo]), reverse=reverso)

    mostrar_carros(carros_ordenados)

    input('\nPressione Enter para voltar.')

#=====MENU DE ALTERAR VEICULOS=====

def menu_alterar_carros():
    while True:
        print('\n======ALTERAR VEÍCULOS======')
        print('\n1 - Marca\n2 - Preço\n3 - Quilometragem\n4 - Ano\n5 - Modelo\n6 - Cor\n0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            alterar_carro('\nDigite a nova marca: ', 'marca', 'texto')
        elif op == 2:
            alterar_carro('\nDigite o novo preço: ', 'preco','numero')
        elif op == 3:
            alterar_carro('\nDigite a nova quilometragem: ', 'quilometragem', 'numero')
        elif op == 4:
            alterar_carro('\nDigite o novo ano: ', 'ano', 'numero')
        elif op == 5:
            alterar_carro('\nDigite o novo modelo:', 'modelo', 'texto')
        elif op == 6:
            alterar_carro('\nDigite a nova cor: ', 'cor', 'texto')
        elif op == 0:
            break
        else:
            print('\nDigite uma opção válida!')

#Altera qualquer informação do veiculo
def alterar_carro(msg,campo,tipo):
    while True:
        if not carros:
            print('\nNenhum veículo cadastrado!')
            break

        mostrar_carros(carros)

        print('\n0 - Voltar')

        op = validacao_int('\nDigite o veículo que desejada alterar: ')

        if op == 0:
            break

        if 1 <= op <= len(carros):
            carro_selecionado = carros[op - 1]
            while True:
                print(f'\nValor atual de {campo}: {carro_selecionado[campo]}')
                print('0 - Voltar.')

                if tipo == 'numero':
                    valor = validacao_int(msg)

                    if valor == 0:
                        break

                elif tipo == 'texto':
                    valor = validacao_texto(msg)

                    if valor == '0':
                        break

                carro_selecionado[campo] = valor

                if campo == 'marca':
                    marcas.clear()
                    for carro in carros:
                        if carro['marca'] not in marcas:
                            marcas.append(carro['marca'])

                print('\nAlteração realizada!')
                salvar_dados(carros)
                break
        else:
            print('Opção inválida')

#======RELÁTIORIOS======

def menu_relatorio():
    while True:
        print('\n======RELÁTORIOS======')
        print('1 - Quantidade de veículos em estoque')
        print('2 - Valor total do estoque')
        print('3 - Veículo mais caro')
        print('4 - Veículo mais barato')
        print('5 - Relatório geral')
        print('0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            relatorio_total_veiculos()
        elif op == 2:
            relatorio_valor_total()
        elif op == 3:
            valor_min_max_veiculos(max)
        elif op == 4:
            valor_min_max_veiculos(min)
        elif op == 5:
            relatorio_geral()
        elif op == 0:
            break
        else:
            print('\nDigite uma opção válida!')

def relatorio_total_veiculos():

    if not carros:
        print('\nNenhum veículo cadastrado!')
        return

    total = len(carros)

    print(f'\nTotal de veículos cadastrados: {total}')

    input('\nPressione Enter para voltar')


def relatorio_valor_total():

    if not carros:
        print('\nNenhum veículo cadastrado!')
        return

    valor_total = sum(carro['preco'] for carro in carros)

    print(f'\nO valor total do estoque é de R${valor_total:,}')

    input('\nPressione Enter para voltar')


def valor_min_max_veiculos(opcao):

    if not carros:
        print('\nNenhum veículo cadastrado!')
        return

    valor = opcao(carros, key=lambda carro: carro['preco'])

    mostrar_carros([valor])

    input('\nPressione Enter para voltar')

def relatorio_geral():
    if not carros:
        print('\nNenhum veículo cadastrado!')
        return

    veiculos_totais = len(carros)
    valor_total = sum(carro['preco'] for carro in carros)
    valor_max = max(carros, key=lambda carro: carro['preco'])
    valor_min = min(carros, key=lambda carro: carro['preco'])

    print(f'Total de carros em estoque: {veiculos_totais}')
    print(f'Valor total do estoque: R${valor_total:,}')
    print('\nVeículo mais caro do estoque:')
    mostrar_carros([valor_max])
    print('\nVeículo mais barato do estoque:')
    mostrar_carros([valor_min])

    input('\nPressione Enter para voltar')