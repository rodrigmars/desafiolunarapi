# Desafio Lunar API

O projeto Desafio Lunar é um puzzle composto por duas partes, um **front-end**(VUEjs) para captação de dados e um **back-end**(Python/Flask) para o processamento lógico. Este repositório compõe apenas API server em Flask para suporte as requisições e processamento no back-end.
O Desafio proposto envolve o desenvolvimento de uma solução capaz de gerênciar os rescursos enviados pelo cliente para armazenamento no lado do server.
API back-end deve receber as requisições e montar as operações CRUD como primeira fase, os próximos desafios envolvem um modelo de negócio para jogo on-line com temática de sobrevivência espacial.

## Pré-requisitos

* Linux / Windows 10 ou superior
* Interpretador python 3.10.8
* ***Possuir chave SSH configurada***

## Mãos à obra - Clonagem e execução

1º Passo - Clone o repositório usando chave SSH:

**Linux**:

```bash
git clone git@github.com:rodrigmars/desafiolunarapi.git && cd desafiolunarapi
```

**Windows**:

```cmd
C:\>git clone git@github.com:rodrigmars/desafiolunarapi.git && cd desafiolunarapi
```

2º Passo - Crie e ative o ambiente virtual com o **venv**:

**Linux**:

```bash
python -m venv env && source env/bin/activate
```

**Windows**:

```cmd
C:\desafiolunarapi>python -m venv env && env\Scripts\activate.bat
```

3º Passo - Instale as dependências:

**Linux**:

```bash
pip install -r requirements-dev.txt
```

**Windows**:

```cmd
C:\desafiolunarapi>pip install -r requirements-dev.txt
```

4º Passo - Para a execução do projeto, lance a instrução conforme o seu terminal:

**Linux**:

```bash
cd desafiolunarapi && flask run
```

**Windows**:

```cmd
C:\desafiolunarapi>cd desafiolunarapi && flask run
```

Com o serviço Flask em execução, o endereço **<http://127.0.0.1:5000>** será disponibilizado conforme saída abaixo.

```bash
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
