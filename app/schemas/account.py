
from pydantic import BaseModel, Field
from datetime import datetime

class AccountBase(BaseModel):
    owner_name: str = Field(..., example="Gabriel Lafis")

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    account_number: str
    balance: float
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

class DepositWithdraw(BaseModel):
    amount: float = Field(..., gt=0, example=50.0)

class Transfer(BaseModel):
    to_account_number: str = Field(..., example="98765-4")
    amount: float = Field(..., gt=0, example=100.0)

