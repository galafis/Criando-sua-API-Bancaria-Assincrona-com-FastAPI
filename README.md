# 🏦 API Bancária Assíncrona com FastAPI | Projeto DIO

Seja muito bem-vindo(a) ao meu projeto de construção de uma **API bancária assíncrona**, desenvolvido com base na trilha de Python da DIO! 🚀

Neste projeto, aplico os principais conceitos de desenvolvimento backend moderno, com ênfase em **alta performance, organização de código e uso de boas práticas com FastAPI**.

## 🎯 Objetivo

Simular operações bancárias básicas como:
- Criação de contas
- Depósitos
- Saques
- Consultas de saldo
- Histórico de transações

## 🧪 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- Uvicorn
- SQLite (via SQLAlchemy)
- Pydantic
- Alembic
- Docker
- Git & GitHub

## 📁 Estrutura do Projeto

📦api-bancaria-fastapi
 ┣ 📂app
 ┃ ┣ 📂models
 ┃ ┣ 📂schemas
 ┃ ┣ 📂services
 ┃ ┣ 📂routes
 ┃ ┗ 📜main.py
 ┣ 📜requirements.txt
 ┣ 📜README.md
 ┗ 📜alembic.ini

## 🚀 Como executar o projeto

```bash
git clone https://github.com/seu-usuario/api-bancaria-fastapi.git
cd api-bancaria-fastapi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## 🔗 Repositório base

[https://github.com/digitalinnovationone/trilha-python-dio](https://github.com/digitalinnovationone/trilha-python-dio)

## 🤝 Como contribuir

1. Fork o projeto
2. Crie uma branch
3. Commit suas alterações
4. Push e abra um Pull Request

## 🧠 Sobre mim

Sou Gabriel Lafis, estudante de Ciência de Dados e entusiasta de desenvolvimento backend com Python.

Feito com 💙 usando FastAPI.
