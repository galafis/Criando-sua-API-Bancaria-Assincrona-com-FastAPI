
# Modelos de Dados

Esta seção descreve os modelos de dados (schemas Pydantic) utilizados na API Bancária Assíncrona.

## `Account`

Representa uma conta bancária no sistema.

```python
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
```

### Campos:

-   `id` (int): Identificador único da conta.
-   `owner_name` (str): Nome do titular da conta.
-   `account_number` (str): Número único da conta bancária.
-   `balance` (float): Saldo atual da conta.
-   `created_at` (datetime): Data e hora de criação da conta.
-   `updated_at` (datetime, opcional): Data e hora da última atualização da conta.

## `AccountCreate`

Schema utilizado para criar uma nova conta. Herda de `AccountBase`.

### Campos:

-   `owner_name` (str): Nome do titular da conta.

## `DepositWithdraw`

Schema utilizado para operações de depósito e saque.

```python
from pydantic import BaseModel, Field

class DepositWithdraw(BaseModel):
    amount: float = Field(..., gt=0, example=50.0)
```

### Campos:

-   `amount` (float): O valor do depósito ou saque. Deve ser maior que zero.

## `Transfer`

Schema utilizado para operações de transferência entre contas.

```python
from pydantic import BaseModel, Field

class Transfer(BaseModel):
    to_account_number: str = Field(..., example="98765-4")
    amount: float = Field(..., gt=0, example=100.0)
```

### Campos:

-   `to_account_number` (str): O número da conta de destino para a transferência.
-   `amount` (float): O valor a ser transferido. Deve ser maior que zero.

