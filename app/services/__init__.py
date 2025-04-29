from app.models import Conta
from sqlalchemy.orm import Session

def criar_conta(db: Session, nome: str, saldo_inicial: float):
    nova_conta = Conta(nome=nome, saldo=saldo_inicial)
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)
    return nova_conta
