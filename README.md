# Sistema de Estoque de Veículos

Projeto desenvolvido em Python para gerenciamento de veículos via terminal, com persistência de dados em JSON.

## Sobre o Projeto

Este projeto foi criado como parte da minha evolução nos estudos de programação Python.

A proposta é desenvolver um sistema próprio e evoluí-lo gradualmente, aplicando novos conceitos conforme avanço nos estudos. Cada versão representa uma etapa prática de aprendizado, organização de código e melhoria das funcionalidades.

## Funcionalidades

* Adicionar veículos
* Listar veículos cadastrados
* Remover veículos com confirmação
* Alterar dados de veículos

  * Marca
  * Modelo
  * Cor
  * Ano
  * Quilometragem
  * Preço
* Buscar veículos por:

  * Marca
  * Modelo
  * Cor
* Filtrar veículos por:

  * Faixa de preço
  * Faixa de quilometragem
  * Ano
* Listar marcas disponíveis no estoque
* Ordenar veículos por:

  * Preço
  * Ano
  * Quilometragem
* Gerar relatórios:

  * Quantidade de veículos cadastrados
  * Valor total do estoque
  * Veículo mais caro
  * Veículo mais barato
  * Relatório geral
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

## Responsabilidades dos Módulos

* `main.py` → menu principal e ponto de entrada do sistema
* `funcoes.py` → regras de negócio e operações principais do sistema
* `dados.py` → leitura e gravação dos dados em JSON
* `config.py` → carregamento inicial dos dados, marcas e constantes
* `utils.py` → validações, confirmações e funções auxiliares

## Tecnologias Utilizadas

* Python 3
* JSON
* Git
* GitHub

## Conceitos Praticados

* Modularização de código
* Funções reutilizáveis
* Listas e dicionários
* Manipulação de arquivos JSON
* Persistência de dados
* Validação de entradas
* Tratamento básico de erros
* Busca em lista de dicionários
* Filtros por intervalo
* Ordenação com `sorted()`, `key`, `lambda` e `reverse`
* Uso de `len()`, `sum()`, `min()` e `max()` em relatórios
* Separação de responsabilidades
* Controle de versão com Git

## Histórico de Versões

### v1.2.0

* Adicionada edição completa dos dados dos veículos
* Criada função genérica para alteração de campos
* Adicionada busca por marca, modelo e cor
* Criada listagem de marcas disponíveis
* Adicionada ordenação por preço, ano e quilometragem
* Adicionado menu de relatórios
* Criados relatórios de quantidade, valor total, veículo mais caro, veículo mais barato e relatório geral
* Melhorada a validação de textos no cadastro
* Adicionada confirmação antes de excluir veículos
* Melhorada a organização das funções por seções

### v1.1.0

* Refatoração completa para arquitetura modular
* Criação dos módulos `dados.py`, `config.py`, `funcoes.py` e `utils.py`
* Implementação de filtros por quilometragem e ano
* Centralização das validações de entrada
* Redução de duplicação de código através de funções reutilizáveis
* Melhor organização e manutenção do projeto

## Próximos Objetivos

* Melhorar validações de ano, preço e quilometragem
* Criar backup automático dos dados
* Tratar arquivo JSON corrompido
* Exportar relatórios para arquivo `.txt`
* Evoluir o projeto para Programação Orientada a Objetos
* Criar testes automatizados futuramente

## Objetivo Profissional

Este projeto faz parte da minha transição e evolução na área de tecnologia, servindo como evidência prática da minha capacidade de estudar, aplicar conceitos, melhorar código existente e evoluir um sistema progressivamente.
