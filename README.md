# Sistema de Estoque de Veículos

Sistema de gerenciamento de veículos desenvolvido em Python e executado pelo terminal.

O projeto permite cadastrar, consultar, alterar, remover, filtrar e ordenar veículos, além de gerar relatórios básicos do estoque. Os dados são armazenados localmente em um arquivo JSON.

## Versão atual

**v1.3.0**

A versão 1.3.0 é focada em melhorias de fluxo, padronização dos menus, validações e experiência de uso no terminal.

## Funcionalidades

- Cadastro de veículos
- Listagem de veículos cadastrados
- Exclusão de veículos com confirmação
- Alteração de:
  - marca
  - modelo
  - cor
  - ano
  - preço
  - quilometragem
- Busca por:
  - marca
  - modelo
  - cor
- Filtros por intervalo de:
  - preço
  - quilometragem
  - ano
- Ordenação por:
  - preço
  - ano
  - quilometragem
- Relatórios com:
  - quantidade de veículos
  - valor total do estoque
  - veículo mais caro
  - veículo mais barato
  - resumo geral
- Persistência automática dos dados em JSON
- Validação de entradas numéricas e textuais
- Validação específica para o ano do veículo
- Limpeza automática da tela durante a navegação
- Títulos padronizados em cada menu

## Melhorias da v1.3.0

- Reformulação do fluxo de alteração de veículos
- Seleção do veículo antes da escolha do campo que será alterado
- Exibição do veículo selecionado durante a alteração
- Exibição do valor atual antes da edição
- Padronização dos títulos das telas
- Limpeza do terminal durante a troca de menus
- Melhorias nas mensagens de sucesso, erro e navegação
- Validação de ano aplicada ao cadastro e à alteração
- Persistência dos dados antes da confirmação final ao usuário
- Redução de repetições por meio de funções reutilizáveis
- Melhor separação de responsabilidades entre as funções

## Estrutura do projeto

```text
.
├── main.py
├── funcoes.py
├── dados.py
├── config.py
├── utils.py
├── carros.json
├── Implementações_futuras.txt
└── README.md
```

### Responsabilidade dos módulos

- `main.py`: menu principal e ponto de entrada do programa
- `funcoes.py`: menus, operações do estoque, filtros, ordenações e relatórios
- `dados.py`: leitura e gravação dos dados em JSON
- `config.py`: carregamento inicial dos veículos e configurações compartilhadas
- `utils.py`: validações, exibição de veículos, títulos e outras funções auxiliares
- `carros.json`: armazenamento local dos veículos cadastrados
- `Implementações_futuras.txt`: ideias registradas para versões futuras

## Requisitos

- Python 3.12 ou superior
- Git, apenas para clonar ou contribuir com o projeto

O projeto utiliza somente módulos da biblioteca padrão do Python, portanto não é necessário instalar dependências externas.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/pauloverleiwork-blip/sistema-estoque-carros-python.git
```

### 2. Acessar a pasta do projeto

```bash
cd sistema-estoque-carros-python
```

### 3. Executar o programa

No Windows:

```bash
py main.py
```

Ou:

```bash
python main.py
```

No Linux ou macOS:

```bash
python3 main.py
```

Caso o arquivo `carros.json` ainda não exista, o sistema iniciará com o estoque vazio e criará o arquivo quando os dados forem salvos.

## Menu principal

```text
======ESTOQUE DE VEÍCULOS======

1 - Adicionar
2 - Deletar
3 - Listar
4 - Filtrar
5 - Alterar veículo
6 - Ordenar veículos
7 - Relatórios
0 - Sair
```

## Tecnologias utilizadas

- Python 3.12
- JSON
- Git
- GitHub

## Conceitos praticados

- Lógica de programação
- Modularização
- Funções reutilizáveis
- Parâmetros e valores de retorno
- Listas e dicionários
- List comprehensions
- Funções `lambda`
- Ordenação com `sorted`
- Operações com `min`, `max`, `sum` e `len`
- Validação de entradas
- Tratamento de exceções
- Manipulação de arquivos JSON
- Persistência de dados
- Separação de responsabilidades
- Refatoração
- Experiência do usuário em aplicações CLI
- Versionamento com Git e GitHub

## Histórico de versões

### v1.3.0

- Reformulação do fluxo de alteração de veículos
- Limpeza da tela entre os menus
- Padronização dos títulos
- Exibição do veículo e do valor atual durante alterações
- Melhorias nas validações, mensagens e navegação
- Refatorações para reduzir repetição e melhorar a manutenção

### v1.2.0

- Implementação de ordenação de veículos
- Criação dos relatórios do estoque
- Expansão das opções de busca e filtragem
- Melhorias na organização das funções

### v1.1.0

- Refatoração para uma arquitetura modular
- Criação dos módulos `dados.py`, `config.py`, `funcoes.py` e `utils.py`
- Centralização das validações
- Persistência dos dados em JSON
- Redução da duplicação de código

## Próximas implementações estudadas

As ideias abaixo fazem parte do planejamento e ainda não representam funcionalidades concluídas:

- Geração dinâmica de menus
- Temas de cores
- Migração para SQLite
- Exportação de relatórios
- Logs
- Testes automatizados
- Interface gráfica

## Objetivo do projeto

Este projeto foi criado como parte da minha jornada de aprendizado em Python.

A proposta é evoluir o mesmo sistema por versões, aplicando novos conhecimentos de programação, organização de código, Git, GitHub e desenvolvimento de software. Dessa forma, o histórico do repositório também registra minha evolução prática.

## Autor

Desenvolvido por **Paulo Verlei**.

GitHub: [pauloverleiwork-blip](https://github.com/pauloverleiwork-blip)
