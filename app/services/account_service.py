
from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate, DepositWithdraw, Transfer
import random

def generate_account_number():
    return f"{random.randint(10000, 99999)}-{random.randint(0, 9)}"

def create_account(db: Session, account: AccountCreate):
    account_number = generate_account_number()
    db_account = Account(owner_name=account.owner_name, account_number=account_number)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account_by_number(db: Session, account_number: str):
    return db.query(Account).filter(Account.account_number == account_number).first()

def deposit_money(db: Session, account_number: str, deposit: DepositWithdraw):
    db_account = get_account_by_number(db, account_number)
    if db_account:
        db_account.balance += deposit.amount
        db.commit()
        db.refresh(db_account)
    return db_account

def withdraw_money(db: Session, account_number: str, withdraw: DepositWithdraw):
    db_account = get_account_by_number(db, account_number)
    if db_account and db_account.balance >= withdraw.amount:
        db_account.balance -= withdraw.amount
        db.commit()
        db.refresh(db_account)
    return db_account

def transfer_money(db: Session, from_account_number: str, transfer: Transfer):
    from_account = get_account_by_number(db, from_account_number)
    to_account = get_account_by_number(db, transfer.to_account_number)

    if from_account and to_account and from_account.balance >= transfer.amount:
        from_account.balance -= transfer.amount
        to_account.balance += transfer.amount
        db.commit()
        db.refresh(from_account)
        db.refresh(to_account)
        return from_account, to_account
    return None, None

