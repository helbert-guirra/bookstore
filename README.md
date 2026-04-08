# 📚 Bookstore

Aplicação **Bookstore** desenvolvida no curso de Backend em Python da EBAC.

---

## 🌐 Deploy

API disponível em: https://bookstore-mtp5.onrender.com

---

## 🚀 Tecnologias utilizadas

- Python 3.5+
- Poetry
- Docker
- Docker Compose
- Django
- Django REST Framework
- PostgreSQL
- GitHub Actions
- Render

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
git clone git@github.com:helbert-guirra/bookstore.git
```

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
docker-compose exec web pytest
```

---

## 🔑 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua-chave-secreta
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 📌 Observações

- Certifique-se de que o Docker esteja rodando antes de executar os comandos.
- O projeto utiliza o Django REST Framework para construção da API.
- Em produção o deploy é feito automaticamente no Render a cada push na branch `main` via GitHub Actions.