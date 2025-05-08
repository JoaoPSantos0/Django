# # 🐍 Projeto Django

Este é um projeto desenvolvido com [Django](https://www.djangoproject.com/)

## 📌 Funcionalidades

- ✅ Cadastro e autenticação de usuários
- ✅ Painel administrativo do Django
- ✅ Integração com banco de dados SQLite
- ✅ Estrutura pronta para deploy e extensões
- ✅ Modularização em apps Django

## 🏗 Estrutura do Projeto

meu_projeto/
├── manage.py
├── meu_projeto/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── app_principal/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
├── db.sqlite3
└── requirements.txt

## 🚀 Como executar

1. Clone o repositório;
2. Crie e ative um ambiente virtual;
3. Instale as dependências: pip install -r requirements.txt;
4. Execute as migrações e inicie o servidor:
   -python manage.py migrate
   -python manage.py runserver
5.http://127.0.0.1:8000/

## Requisitos
Python 3.x

1.Django 4.x ou superior

2.SQLite (padrão, sem dependências externas)


