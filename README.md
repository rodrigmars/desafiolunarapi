# Desafio Lunar API

Este projeto é um puzzle composto por duas partes, um **front-end**(VUEjs) para captação de dados e um **back-end**(Python/Flask) para o processamento lógico.
O Desafio proposto é desenvolver e manter uma solução capaz de gerênciar os rescursos(minérios) identificados em solo lunar.
API back-end deve receber as requisições e montar as operações CRUD(Create, Read, Update, Delete) para o gerênciamento de dados como primeira fase, os próximos desafios deverão compor um modelo de jogo on-line para o tema de sobrevivência espacial.

## Pré-requisito

* Python 3.10.8
* Linux

## Mãos à obra - Como baixar e executar

1º Passo - Clone o repositório:

    ```bash
    $ git clone git@github.com:rodrigmars/desafiolunarapi.git && cd desafiolunarapi

2º Passo - Crie e ative o ambiente virtual com o **venv**:

    ```bash
    $ python -m venv env && source env/bin/activate

3º Passo - Instale as dependências:

    ```bash
    $ pip install -r requirements-dev.txt

4º Passo - Após a instalação dos pacotes, execute o projeto conforme a instrução:

    ```bash
    $ cd desafiolunarapi && flask run
