from pydantic import BaseModel

class ContaCreate(BaseModel):
    nome: str
    saldo_inicial: float

class Conta(BaseModel):
    id: int
    nome: str
    saldo: float

    class Config:
        orm_mode = True
