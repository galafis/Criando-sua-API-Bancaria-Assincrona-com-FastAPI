
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.account import Account

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_account():
    response = client.post(
        "/contas/",
        json={"owner_name": "Test Account"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["owner_name"] == "Test Account"
    assert "account_number" in data
    assert data["balance"] == 0.0
    assert "id" in data

def test_get_account_details():
    # Primeiro cria uma conta para buscar
    response = client.post(
        "/contas/",
        json={"owner_name": "Another Test Account"}
    )
    account_number = response.json()["account_number"]

    response = client.get(f"/contas/{account_number}")
    assert response.status_code == 200
    data = response.json()
    assert data["owner_name"] == "Another Test Account"
    assert data["account_number"] == account_number

def test_get_non_existent_account():
    response = client.get("/contas/99999-9")
    assert response.status_code == 404
    assert response.json() == {"detail": "Conta não encontrada"}

def test_deposit_money():
    # Primeiro cria uma conta
    response = client.post(
        "/contas/",
        json={"owner_name": "Deposit Account"}
    )
    account_number = response.json()["account_number"]

    response = client.post(
        f"/contas/{account_number}/deposito",
        json={"amount": 150.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["balance"] == 150.0

def test_withdraw_money():
    # Primeiro cria uma conta e deposita
    response = client.post(
        "/contas/",
        json={"owner_name": "Withdraw Account"}
    )
    account_number = response.json()["account_number"]
    client.post(
        f"/contas/{account_number}/deposito",
        json={"amount": 200.0}
    )

    response = client.post(
        f"/contas/{account_number}/saque",
        json={"amount": 50.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["balance"] == 150.0

def test_withdraw_insufficient_funds():
    # Primeiro cria uma conta e deposita pouco
    response = client.post(
        "/contas/",
        json={"owner_name": "Insufficient Funds Account"}
    )
    account_number = response.json()["account_number"]
    client.post(
        f"/contas/{account_number}/deposito",
        json={"amount": 30.0}
    )

    response = client.post(
        f"/contas/{account_number}/saque",
        json={"amount": 100.0}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Saldo insuficiente"}

def test_transfer_money():
    # Cria duas contas e deposita na primeira
    response_from = client.post(
        "/contas/",
        json={"owner_name": "From Account"}
    )
    from_account_number = response_from.json()["account_number"]
    client.post(
        f"/contas/{from_account_number}/deposito",
        json={"amount": 300.0}
    )

    response_to = client.post(
        "/contas/",
        json={"owner_name": "To Account"}
    )
    to_account_number = response_to.json()["account_number"]

    response = client.post(
        f"/contas/{from_account_number}/transferencia",
        json={
            "to_account_number": to_account_number,
            "amount": 100.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["account_number"] == from_account_number
    assert data[0]["balance"] == 200.0
    assert data[1]["account_number"] == to_account_number
    assert data[1]["balance"] == 100.0

def test_transfer_insufficient_funds():
    # Cria duas contas e deposita pouco na primeira
    response_from = client.post(
        "/contas/",
        json={"owner_name": "From Insufficient Account"}
    )
    from_account_number = response_from.json()["account_number"]
    client.post(
        f"/contas/{from_account_number}/deposito",
        json={"amount": 50.0}
    )

    response_to = client.post(
        "/contas/",
        json={"owner_name": "To Insufficient Account"}
    )
    to_account_number = response_to.json()["account_number"]

    response = client.post(
        f"/contas/{from_account_number}/transferencia",
        json={
            "to_account_number": to_account_number,
            "amount": 100.0
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Saldo insuficiente na conta de origem"}


def test_transfer_non_existent_to_account():
    # Cria uma conta e tenta transferir para uma inexistente
    response_from = client.post(
        "/contas/",
        json={"owner_name": "From Non Existent Account"}
    )
    from_account_number = response_from.json()["account_number"]
    client.post(
        f"/contas/{from_account_number}/deposito",
        json={"amount": 100.0}
    )

    response = client.post(
        f"/contas/{from_account_number}/transferencia",
        json={
            "to_account_number": "99999-9",
            "amount": 50.0
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Conta de destino não encontrada"}

