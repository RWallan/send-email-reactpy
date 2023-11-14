# Enviar e-mail usando ReactPy & FastAPI

Este projeto demonstra como utilizar o Python para construir uma aplicação full-stack utilizando ReactPy e FastAPI que envia o Zen do Python por e-mail utilizando uma conta Gmail.

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

**Obs:** Para executar o backend, é necessário que possua um arquivo `.env` com as seguintes informações:

    MAIL_TOKEN: str # Token do gmail para possibilitar o envio por API.
    MAIL_FROM: str # Email pertencente ao token que irá enviar as mensagens.

Atualmente o projeto aceita apenas envio de e-mails por uma conta Gmail.

## Executando via Docker [WIP]

WIP.

# To do

[ ] Execução via Docker

[ ] Documentação das APIs

[ ] Construir testes para o frontend

[ ] Construir testes para o backend

# Colaboração

Pull requests e Issues são bem vindos para este projeto!

# Licença

Este projeto está sob a licença MIT.