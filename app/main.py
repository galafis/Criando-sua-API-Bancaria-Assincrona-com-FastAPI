from fastapi import FastAPI
from app.routes import contas

app = FastAPI(title="API Bancária Assíncrona - DIO")

app.include_router(contas.router)
