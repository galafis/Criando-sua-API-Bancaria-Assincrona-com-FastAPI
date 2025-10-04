from fastapi import FastAPI
from app.routes import contas
from app.database import Base, engine
from app.models import account

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Bancária Assíncrona - DIO")

app.include_router(contas.router)

