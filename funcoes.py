
from config import carros, marcas, modulos_str, modulos_int
from dados import salvar_dados
from utils import validacao_int, validacao_texto, mostrar_carros, confirmar_acao, validacao_ano, verificar_veiculos, mostrar_titulo, limpar_tela

#=====ADICIONA VEICULOS AO ESTOQUE=====

def adicionar_carro():

    mostrar_titulo('ADICIONAR VEÍCULO')
    novo_carro = {}

    for modulo in modulos_str:
        valor = validacao_texto(f'Digite {modulo}: ')
        novo_carro[modulo] = valor

    for modulo in modulos_int:
        valor = validacao_int(f'Digite {modulo}: ')
        novo_carro[modulo] = valor

    valor = validacao_ano('Digite o ano: ')
    novo_carro['ano'] = valor


    carros.append(novo_carro)
    salvar_dados(carros)

    if novo_carro['marca'] not in marcas:
        marcas.append(novo_carro['marca'])

#=====DELETA VEICULOS DO ESTOQUE=====

def deletar_carro():
    while True:
        if verificar_veiculos():
            return

        mostrar_titulo('DELETAR VEÍCULO')

        mostrar_carros(carros)

        print('\n0 - Voltar')

        op = validacao_int('\nDigite: ')

        if op == 0:
            break

        if 1 <= op <= len(carros):

            carro_selecionado = carros[op - 1]

            mostrar_titulo('VEÍCULO SELECIONADO')
            mostrar_carros([carro_selecionado])
            if confirmar_acao("\nTem certeza que deseja deletar o veículo? [S/N]: "):
                carro_removido = carros.pop(op - 1)
                print('\nOperação realizada com sucesso!')
                input('\nPressione Enter para continuar.')


                marca_removida = carro_removido['marca']
                if not any(carro['marca'] == marca_removida for carro in carros):
                    marcas.remove(marca_removida)

                salvar_dados(carros)
                return
            else:
                print('\nOperação cancelada!')
                input('\nPressione Enter para continuar.')
        else:
            print(f'\nDigite uma opção entre 0 e {len(carros)}')

#=====LISTAS=====

#lista todos os veiculos do estoque
def listar_carros():
    if verificar_veiculos():
        return

    mostrar_titulo('LISTAR VEÍCULOS')

    mostrar_carros(carros)

    input('\nPressione Enter para voltar.')

#Lista marcas disponiveis no estoque
def listar_marcas():
    if verificar_veiculos():
        return

    mostrar_titulo('MOSTRAR MARCAS')

    for marca in marcas:
       print(f'- {marca}')

    input('\nPressione Enter para continuar.')

#=====MENU DE FILTRO DE VEICULOS=====

def menu_filtrar_carros():
    while True:
        mostrar_titulo('FILTRAR VEÍCULOS')
        print('\n1 - Marca\n2 - Preço\n3 - Quilometragem\n4 - Ano\n5 - Modelo\n6 - Cor\n7 - Listar marcas disponíveis\n0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            mostrar_titulo('FILTRAR VEÍCULOS')
            buscar_carro('\nDigite a marca desejada: ', 'marca')
        elif op == 2:
            mostrar_titulo('FILTRAR VEÍCULOS')
            filtrar_carro("\nDigite o valor mínimo: R$", "Digite o valor máximo: R$", "preco")
        elif op == 3:
            mostrar_titulo('FILTRAR VEÍCULOS')
            filtrar_carro("\nDigite a quilometragem mínima: ","Digite a quilometragem máxima: ", "quilometragem")
        elif op == 4:
            mostrar_titulo('FILTRAR VEÍCULOS')
            filtrar_carro('\nDigite o ano mínimo: ', 'Digite o ano máximo: ', 'ano')
        elif op == 5:
            mostrar_titulo('FILTRAR VEÍCULOS')
            buscar_carro('\nDigite o modelo desejado: ', 'modelo')
        elif op == 6:
            mostrar_titulo('FILTRAR VEÍCULOS')
            buscar_carro('\nDigite a cor desejada: ', 'cor')
        elif op == 7:
            mostrar_titulo('FILTRAR VEÍCULOS')
            listar_marcas()
        elif op == 0:
            break
        else:
            print('\nDigite uma opção entre 0 e 7.')

#=====FILTROS DE VEICULOS=====#

#Filtra veiculos por cor, modelo e marca
def buscar_carro(msg, campo):

    if verificar_veiculos():
        return

    termo_busca = validacao_texto(msg)

    carros_filtrados = [
        carro for carro in carros
        if termo_busca in carro[campo].upper()
    ]

    if not carros_filtrados:
        print('\nNenhum veículo corresponde ao filtro.')
        input('\nPressione Enter para continuar.')
        return
    else:
        mostrar_titulo('VEÍCULO FILTRADO')
        mostrar_carros(carros_filtrados)

    input('\nPressione Enter para voltar.')

#filtra veiculos por minimo e maximo, ano, preço e quilometragem
def filtrar_carro(msg_min, msg_max, campo):
    while True:
        if verificar_veiculos():
            return

        minimo = validacao_int(msg_min)

        maximo = validacao_int(msg_max)

        if minimo > maximo:
            print('\nO valor minimo não pode ser maior que o valor máximo.')
            input('\nPressione Enter para continuar.')
            return

        carros_filtrados = [
            carro for carro in carros
            if minimo <= carro[campo] <= maximo
        ]

        if not carros_filtrados:
            print('\nNenhum veículo corresponde ao filtro.')
            input('\nPressione Enter para continuar.')
            return
        else:
            mostrar_titulo('VEÍCULO FILTRADO')
            mostrar_carros(carros_filtrados)

        input('\nPressione Enter para voltar.')
        break

#=====MENU ORDENAR VEICULOS=====

def menu_ordenar_carros():
    while True:
        mostrar_titulo('ORDENAR VEÍCULOS')
        print('\n1 - Preço: menor para maior\n2 - Preço: maior para menor\n3 - Ano: mais antigo para mais novo\n4 - Ano: mais novo para mais antigo\n5 - Quilometragem: menor para maior\n6 - Quilometragem: maior para menor\n0 - Voltar')
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
            print('\nDigite uma opção entre 0 e 6.')

#Função de ordenação de veiculos

def ordenar_carros(campo, reverso):
    if verificar_veiculos():
        return

    carros_ordenados = sorted(carros, key=lambda carro: int(carro[campo]), reverse=reverso)
    mostrar_titulo('VEÍCULOS ORDENADOS')
    mostrar_carros(carros_ordenados)

    input('\nPressione Enter para voltar.')

#=====MENU DE ALTERAR VEICULOS=====
def menu_alterar_veiculos():
        while True:
            if verificar_veiculos():
                return

            mostrar_titulo('ALTERAR VEÍCULOS')
            mostrar_carros(carros)

            print('\n0 - Voltar')

            op = validacao_int('\nDigite o veículo que deseja alterar: ')

            if op == 0:
                break

            if 1 <= op <= len(carros):
                carro_selecionado = carros[op - 1]
                menu_opcoes_alterar_veiculos(carro_selecionado)
        else:
            print(f'\nSelecione uma opção entre 0 e {len(carros)}.')


def menu_opcoes_alterar_veiculos(veiculo):
    while True:
        mostrar_titulo('OPÇÕES DE ALTERAÇÃO')
        print('\n1 - Marca\n2 - Preço\n3 - Quilometragem\n4 - Ano\n5 - Modelo\n6 - Cor\n0 - Voltar')
        op = validacao_int('\nDigite: ')

        if op == 1:
            alterar_veiculo('\nDigite a nova marca: ', 'marca', 'texto',veiculo)
        elif op == 2:
            alterar_veiculo('\nDigite o novo preço: ', 'preco','numero',veiculo)
        elif op == 3:
            alterar_veiculo('\nDigite a nova quilometragem: ', 'quilometragem', 'numero',veiculo)
        elif op == 4:
            alterar_veiculo('\nDigite o novo ano: ', 'ano', 'numero',veiculo)
        elif op == 5:
            alterar_veiculo('\nDigite o novo modelo:', 'modelo', 'texto',veiculo)
        elif op == 6:
            alterar_veiculo('\nDigite a nova cor: ', 'cor', 'texto',veiculo)
        elif op == 0:
            break
        else:
            print('\nDigite uma opção entre 0 e 6.')

#Altera qualquer informação do veiculo
def alterar_veiculo(msg,campo,tipo,veiculo):
    while True:
        if tipo == 'numero':
            valor = validacao_int(msg)

            if valor == 0:
                break

        elif tipo == 'texto':
            valor = validacao_texto(msg)

            if valor == '0':
                break

        veiculo[campo] = valor

        if campo == 'marca':
            marcas.clear()
            for carro in carros:
                if carro['marca'] not in marcas:
                    marcas.append(carro['marca'])

        print('\nVeículo atualizado com sucesso!')
        input('\nPressione Enter para continuar.')
        salvar_dados(carros)
        break

#======RELATÓRIOS======

def menu_relatorio():
    while True:
        mostrar_titulo('RELATÓRIOS')
        print('\n1 - Quantidade de veículos em estoque\n2 - Valor total do estoque\n3 - Veículo mais caro\n4 - Veículo mais barato\n5 - Relatório geral\n0 - Voltar')
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
            print('\nDigite uma opção entre 0 e 5.')

def relatorio_total_veiculos():
    if verificar_veiculos():
        return

    total = len(carros)

    print(f'\nTotal de veículos cadastrados: {total}')

    input('\nPressione Enter para voltar')


def relatorio_valor_total():
    if verificar_veiculos():
        return

    valor_total = sum(carro['preco'] for carro in carros)

    print(f'\nO valor total do estoque é de R${valor_total:,}')

    input('\nPressione Enter para voltar')


def valor_min_max_veiculos(opcao):
    if verificar_veiculos():
        return

    valor = opcao(carros, key=lambda carro: carro['preco'])

    mostrar_carros([valor])

    input('\nPressione Enter para voltar')

def relatorio_geral():
    if verificar_veiculos():
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