from funcoes import adicionar_carro,deletar_carro,listar_carros,menu_filtrar_carros,alterar_preco
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
            menu_filtrar_carros()
        elif op == '5':
            alterar_preco()
        elif op == '0':
            break
        else:
            print('\nDigite uma opção válida!')

if __name__ == '__main__':
    menu_principal()