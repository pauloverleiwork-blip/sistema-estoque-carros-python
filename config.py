from dados import carregar_dados, salvar_dados

#carrega os dados ao iniciar
carros = carregar_dados()

#Atualiza a lista de marcas
def atualizar_marcas():
    marcas = []
    for carro in carros:
        if carro['marca'] not in marcas:
            marcas.append(carro['marca'])
    return marcas

marcas = atualizar_marcas()

#Contantes
MODULOS = ['marca', 'modelo', 'cor']