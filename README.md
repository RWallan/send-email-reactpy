# Enviar e-mail usando ReactPy & FastAPI

Este projeto demonstra como utilizar o Python para construir uma aplicação full-stack utilizando ReactPy e FastAPI.

O ReactPy é responsável por criar o frontend, simulando a mesma estrutura do React, utilizando uma sintaxe puramente 'pytônica'. O FastAPI é uma biblioteca moderna e de alta performance responsável pelo backend da aplicação.

# Requisitos

Python 3.11.

As principais bibliotecas que esse projeto foi construído são:

* FastAPI
* ReactPy

# Instalação

É recomendado o uso do Poetry para o gerenciamento de dependências.

## Clonando o repositório e instalando dependências

Para poder utilizar as funcionalidades do repositório, primeiramente clone o repositório:

```bash
git clone https://github.com/RWallan/send-email-reactpy
```

E instale as dependências:

```bash
cd ./send-email-reactpy/
```

```bash
poetry install
```

## Executando via terminal

Para executar o projeto via terminal abra dois terminais: Um para a aplicação frontend e outro para a aplicação backend.

Em um dos terminais, execute os comandos:

```bash
cd frontend/
```

```bash
poetry run task frontend
```

E no outro:

```bash
cd backend/
```

```bash
poetry run task backend
```

## Executando via Docker [WIP]

WIP.

# To do

[ ] Execução via Docker

[ ] Documentação das APIs

# Licença

Este projeto está sob a licença MIT.