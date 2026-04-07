# 📚 Bookstore

Aplicação **Bookstore** desenvolvida no curso de Backend em Python da EBAC.

---

## 🚀 Tecnologias utilizadas

- Python 3.5+
- Poetry
- Docker
- Docker Compose
- Django

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- Python 3.5 ou superior
- Poetry
- Docker
- Docker Compose

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone git@github.com:drsantos20/bookstore.git
````

Acesse a pasta do projeto:

```bash
cd bookstore
```

Instale as dependências:

```bash
poetry install
```

---

## ▶️ Executando o projeto (ambiente local)

Aplique as migrações:

```bash
poetry run python manage.py migrate
```

Inicie o servidor:

```bash
poetry run python manage.py runserver
```

---

## 🐳 Executando com Docker

Suba os containers:

```bash
docker-compose up -d --build
```

Execute as migrações:

```bash
docker-compose exec web python manage.py migrate
```

---

## 🧪 Rodando os testes

Execute os testes dentro do container:

```bash
docker-compose exec web python manage.py test
```

---

## 📌 Observações

* Certifique-se de que o Docker esteja rodando antes de executar os comandos.
* O projeto utiliza o Django como framework principal.

```

Se quiser, depois posso te ajudar a deixar isso ainda mais forte pra recrutador (com descrição do problema, features e prints).
```
