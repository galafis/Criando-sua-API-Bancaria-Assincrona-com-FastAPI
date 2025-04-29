from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ContaCreate, Conta
from app.services import criar_conta

router = APIRouter(prefix="/contas", tags=["Contas"])

def get_db():
    # Simulação de dependência do banco (substituir por Session real)
    from sqlalchemy.orm import Session
    yield Session()

@router.post("/", response_model=Conta)
def criar(conta: ContaCreate, db: Session = Depends(get_db)):
    return criar_conta(db, conta.nome, conta.saldo_inicial)
