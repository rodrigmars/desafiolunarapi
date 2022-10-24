# Desafio Lunar API

O projeto Desafio Lunar é um puzzle composto por duas partes, um **front-end**(VUEjs) para captação de dados e um **back-end**(Python/Flask) para o processamento lógico. Este repositório compõe apenas API server em Flask para suporte as requisições e processamento no back-end.
O Desafio proposto envolve o desenvolvimento de uma solução capaz de gerênciar os rescursos enviados pelo cliente para armazenamento no lado do server.
API back-end deve receber as requisições e montar as operações CRUD como primeira fase, os próximos desafios devem compor um modelo de jogo on-line com temática de sobrevivência espacial.

## Pré-requisito

* Interpretador python 3.10.8
* Linux / Windows 10 ou superior

## Mãos à obra - Como baixar e executar

1º Passo - Clone o repositório:

    ```bash
    $ git clone git@github.com:rodrigmars/desafiolunarapi.git && cd desafiolunarapi
    
    ```cmd
    C:\>git clone git@github.com:rodrigmars/desafiolunarapi.git && cd desafiolunarapi

2º Passo - Crie e ative o ambiente virtual com o **venv**:

    ```bash
    $ python -m venv env && source env/bin/activate
    
    ```cmd
    C:\desafiolunarapi>python -m venv env && env\Scripts\activate.bat

3º Passo - Instale as dependências:

    ```bash
    $ pip install -r requirements-dev.txt

    ```cmd
    C:\desafiolunarapi>pip install -r requirements-dev.txt

4º Passo - Após a instalação dos pacotes, execute o projeto conforme a instrução:

    ```bash
    $ cd desafiolunarapi && flask run

    ```cmd
    C:\desafiolunarapi>cd desafiolunarapi && flask run
