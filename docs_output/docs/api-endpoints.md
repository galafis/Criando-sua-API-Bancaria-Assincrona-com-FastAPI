
# Endpoints da API

Esta seção detalha todos os endpoints disponíveis na API Bancária Assíncrona, incluindo seus métodos HTTP, URLs, descrições e os schemas de requisição e resposta esperados.

## Contas

Todos os endpoints relacionados a contas bancárias estão sob o prefixo `/contas`.

### `POST /contas/` - Criar Nova Conta

Cria uma nova conta bancária com um nome de titular especificado.

-   **Método:** `POST`
-   **URL:** `/contas/`
-   **Descrição:** Registra uma nova conta bancária.
-   **Schema de Requisição:** `AccountCreate`
    ```json
    {
      "owner_name": "Gabriel Lafis"
    }
    ```
-   **Schema de Resposta:** `Account`
    ```json
    {
      "id": 1,
      "owner_name": "Gabriel Lafis",
      "account_number": "12345-6",
      "balance": 0.0,
      "created_at": "2023-10-27T10:00:00.000Z",
      "updated_at": "2023-10-27T10:00:00.000Z"
    }
    ```

### `GET /contas/{account_number}` - Obter Detalhes da Conta

Retorna os detalhes de uma conta bancária específica usando seu número de conta.

-   **Método:** `GET`
-   **URL:** `/contas/{account_number}`
-   **Descrição:** Recupera informações de uma conta.
-   **Parâmetros de Path:**
    -   `account_number` (string): O número da conta bancária.
-   **Schema de Resposta:** `Account`

### `POST /contas/{account_number}/deposito` - Realizar Depósito

Realiza um depósito em uma conta bancária especificada.

-   **Método:** `POST`
-   **URL:** `/contas/{account_number}/deposito`
-   **Descrição:** Adiciona fundos a uma conta.
-   **Parâmetros de Path:**
    -   `account_number` (string): O número da conta bancária.
-   **Schema de Requisição:** `DepositWithdraw`
    ```json
    {
      "amount": 100.0
    }
    ```
-   **Schema de Resposta:** `Account`

### `POST /contas/{account_number}/saque` - Realizar Saque

Realiza um saque de uma conta bancária especificada, com validação de saldo.

-   **Método:** `POST`
-   **URL:** `/contas/{account_number}/saque`
-   **Descrição:** Retira fundos de uma conta.
-   **Parâmetros de Path:**
    -   `account_number` (string): O número da conta bancária.
-   **Schema de Requisição:** `DepositWithdraw`
-   **Schema de Resposta:** `Account`

### `POST /contas/{from_account_number}/transferencia` - Realizar Transferência

Realiza uma transferência de fundos entre duas contas bancárias, com validação de saldo na conta de origem.

-   **Método:** `POST`
-   **URL:** `/contas/{from_account_number}/transferencia`
-   **Descrição:** Transfere fundos de uma conta para outra.
-   **Parâmetros de Path:**
    -   `from_account_number` (string): O número da conta de origem.
-   **Schema de Requisição:** `Transfer`
    ```json
    {
      "to_account_number": "98765-4",
      "amount": 50.0
    }
    ```
-   **Schema de Resposta:** `List[Account]` (retorna as contas de origem e destino atualizadas)

