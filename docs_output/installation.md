
# Guia de Instalação

Este guia detalha os passos necessários para configurar e executar a API Bancária Assíncrona localmente.

## Pré-requisitos

Certifique-se de ter o seguinte software instalado em sua máquina:

-   **Python 3.11+**
-   **Git**

## Passos para Instalação

1.  **Clone o repositório:**

    Abra seu terminal e execute o comando para clonar o projeto:

    ```bash
    git clone https://github.com/galafis/Criando-sua-API-Bancaria-Assincrona-com-FastAPI.git
    cd Criando-sua-API-Bancaria-Assincrona-com-FastAPI
    ```

2.  **Crie e ative o ambiente virtual:**

    É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python -m venv venv
    # No Linux/macOS:
    source venv/bin/activate
    # No Windows (PowerShell):
    # .\venv\Scripts\Activate.ps1
    # No Windows (Command Prompt):
    # venv\Scripts\activate.bat
    ```

3.  **Instale as dependências:**

    Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**

    Crie um arquivo chamado `.env` na raiz do projeto e adicione a URL do banco de dados. Para desenvolvimento local, SQLite é uma boa opção:

    ```ini
    DATABASE_URL=sqlite:///./sql_app.db
    ```

5.  **Execute as migrações do banco de dados:**

    O projeto utiliza Alembic para gerenciar as migrações do banco de dados. Execute o seguinte comando para criar as tabelas necessárias:

    ```bash
    alembic upgrade head
    ```

6.  **Inicie a aplicação:**

    Finalmente, inicie o servidor FastAPI usando Uvicorn:

    ```bash
    uvicorn app.main:app --reload
    ```

    A API estará acessível em `http://localhost:8000`. Você pode interagir com a documentação interativa (Swagger UI) em `http://localhost:8000/docs` e a documentação ReDoc em `http://localhost:8000/redoc`.

