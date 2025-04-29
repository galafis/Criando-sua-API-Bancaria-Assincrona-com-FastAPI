from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    saldo = Column(Float)
