# Sistema de Estoque de Veículos

Projeto desenvolvido em Python para gerenciamento de veículos via terminal, com persistência de dados em JSON.

## Funcionalidades

* Adicionar veículos
* Listar veículos
* Remover veículos
* Alterar preço de veículos
* Filtrar por marca
* Filtrar por faixa de preço
* Filtrar por quilometragem
* Filtrar por ano
* Persistência automática dos dados em JSON

## Estrutura do Projeto

```text
.
├── main.py
├── funcoes.py
├── dados.py
├── config.py
├── utils.py
└── carros.json
```

### Responsabilidades dos módulos

* `main.py` → menu principal e ponto de entrada do sistema
* `funcoes.py` → regras de negócio e operações do sistema
* `dados.py` → leitura e gravação dos dados em JSON
* `config.py` → configurações e carregamento inicial dos dados
* `utils.py` → validações e funções auxiliares

## Tecnologias Utilizadas

* Python 3
* JSON

## Conceitos Praticados

* Modularização de código
* Manipulação de arquivos JSON
* Persistência de dados
* Funções reutilizáveis
* Validação de entradas
* Estruturas de dados (listas e dicionários)
* Separação de responsabilidades

## Objetivo

Este projeto foi desenvolvido como parte da minha jornada de aprendizado em programação Python.

A cada nova versão, o sistema recebe melhorias de estrutura, organização e funcionalidades, servindo como evidência prática da evolução dos meus conhecimentos em desenvolvimento de software.

## Histórico de Versões

### v1.1.0

* Refatoração completa para arquitetura modular
* Criação dos módulos `dados.py`, `config.py`, `funcoes.py` e `utils.py`
* Implementação de filtros por quilometragem e ano
* Centralização das validações de entrada
* Redução de duplicação de código através de funções reutilizáveis
* Melhor organização e manutenção do projeto
