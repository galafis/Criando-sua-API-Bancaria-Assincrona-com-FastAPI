from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.account import AccountCreate, Account, DepositWithdraw, Transfer
from app.services import account_service
from app.database import get_db

router = APIRouter(prefix="/contas", tags=["Contas"])

@router.post("/", response_model=Account, status_code=status.HTTP_201_CREATED)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db)):
    return account_service.create_account(db=db, account=account)

@router.get("/{account_number}", response_model=Account)
def get_account_details(account_number: str, db: Session = Depends(get_db)):
    db_account = account_service.get_account_by_number(db, account_number)
    if db_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")
    return db_account

@router.post("/{account_number}/deposito", response_model=Account)
def deposit_to_account(account_number: str, deposit: DepositWithdraw, db: Session = Depends(get_db)):
    db_account = account_service.deposit_money(db, account_number, deposit)
    if db_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")
    return db_account

@router.post("/{account_number}/saque", response_model=Account)
def withdraw_from_account(account_number: str, withdraw: DepositWithdraw, db: Session = Depends(get_db)):
    db_account = account_service.get_account_by_number(db, account_number)
    if db_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")
    if db_account.balance < withdraw.amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Saldo insuficiente")
    db_account = account_service.withdraw_money(db, account_number, withdraw)
    return db_account

@router.post("/{from_account_number}/transferencia", response_model=list[Account])
def transfer_between_accounts(from_account_number: str, transfer: Transfer, db: Session = Depends(get_db)):
    from_account = account_service.get_account_by_number(db, from_account_number)
    if from_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta de origem não encontrada")
    
    to_account = account_service.get_account_by_number(db, transfer.to_account_number)
    if to_account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta de destino não encontrada")

    if from_account.balance < transfer.amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Saldo insuficiente na conta de origem")

    from_account, to_account = account_service.transfer_money(db, from_account_number, transfer)
    return [from_account, to_account]

