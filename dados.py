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

def salvar_dados(carros):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(carros, arquivo, indent=2, ensure_ascii=False) ,