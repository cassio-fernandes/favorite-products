# 🛍️ Product Favorites API

API desenvolvida em **Django REST Framework** que permite que clientes favoritem produtos.  
Os produtos são obtidos da **API externa** https://fakestoreapi.com/.

---

## 📌 Funcionalidades

- 🔎 Listar produtos disponíveis
- ⭐ Favoritar produtos por cliente
- 🗂️ Listar produtos favoritados
- 🔐 Autenticação de usuários

---

## 🏗️ Arquitetura

- **Backend:** Django + Django REST Framework
- **Cache:** Redis
- **Banco de Dados:** PostgreSQL
- **Containerização:** Docker + docker-compose
- **API externa:** [Fake Store API](https://fakestoreapi.com/)

---

## ⚙️ Pré-requisitos

- Python 3.11+
- Docker e Docker Compose
- Redis
- PostgreSQL

> **Obs.:** Apesar de estar em container Docker, pode ser necessário realizar configurações extras para execução via **Docker Desktop**.

## Setup do projeto

### 1. Clonar o repositório
```bash

$ git clone https://github.com/cassio-fernandes/favorite-products.git
cd favorite-products
```

### 2. Criar migrações
```bash
$ make migrate
```

### 3. Executar projeto
```bash
$ make run-build # para forçar build da imagem OU
$ make run # apenas recria os containers
```

### 4. Criar usuário (Admin para gerenciar clientes)
```bash
$ make createsuperuser
```

#### As informações de email e senha serão utilizados para realizar o login na API

## Endpoints da API

### Gerar Token de acesso
```bash
$ $ curl --location 'http://localhost:8000/aiqfome/v1/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "jonsnow@gmail.com",
    "password": "123456"
}'
```
#### substitua o data-raw pelo usuário e senha criados no step 4

### Criar novo cliente
```bash
$ curl --location 'http://localhost:8000/aiqfome/v1/clients/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2MjA5NzYxLCJpYXQiOjE3NTYyMDk0NjEsImp0aSI6ImQ1YzIwODE3NTZhMTQzNzBiYmNjMjk0ZmM2MWQ4ZjY4IiwidXNlcl9pZCI6IjUifQ.ov9RkX-k-VYaW6stkYXc_VWe8GUlysefgZk7N_AopyM' \
--data-raw '{
    "name": "daenerys",
    "email": "kaleesy@gmal.com",
    "password": "drogoS2"
}'
```
### Editar novo cliente
```bash
$ curl --location --request PATCH 'http://localhost:8000/aiqfome/v1/clients/382be7d4-4a34-40e1-9725-f2c51f34db24/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2MjEwNjk3LCJpYXQiOjE3NTYyMTAzOTcsImp0aSI6IjBiNjNiMzQ2ODdjYzQzYjNiZjJmMWY5NjdiZThmY2MwIiwidXNlcl9pZCI6IjUifQ.K52neQ9Me_kdgzho-5I-od1sK7NjY9Z54yVSVClYB8U' \
--data '{
    "name": "The mother of dragons"
}'
```
### Visualizar e favoritar produtos
```bash
$ curl --location 'http://localhost:8000/aiqfome/v1/favorite-products' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2MjExMTU1LCJpYXQiOjE3NTYyMTA4NTUsImp0aSI6IjE5ZGRjMGJlYTNjMzQzNDk4NDMyMTU2MmI3YTRlOTYxIiwidXNlcl9pZCI6IjUifQ.8aCG6luIeyyNJU3KmY9ckrc8uTUyu_bEqyD6m2h0yLA' \

$ curl --location 'http://localhost:8000/aiqfome/v1/favorite-products/favorite/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2MjExMTU1LCJpYXQiOjE3NTYyMTA4NTUsImp0aSI6IjE5ZGRjMGJlYTNjMzQzNDk4NDMyMTU2MmI3YTRlOTYxIiwidXNlcl9pZCI6IjUifQ.8aCG6luIeyyNJU3KmY9ckrc8uTUyu_bEqyD6m2h0yLA' \
--data '{
    "product_ids": [2,13,14]
}'
```
### Visualizar produtos favoritados
```bash
curl --location 'http://localhost:8000/aiqfome/v1/favorite-products' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU2MjExNDc2LCJpYXQiOjE3NTYyMTExNzYsImp0aSI6IjljODZlMDA0ZTAxZjQxOGRiOWVjZmU3ZjY3ZDUxY2M4IiwidXNlcl9pZCI6IjUifQ.NG36gh01eVtdv4O50cMWLN4SkkAmA_IK7aYTwGb6xFw' \
}'
```
