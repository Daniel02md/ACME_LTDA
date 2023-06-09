# ACME_LTDA
## Teste da API com Front End
```
https://daniel02md.github.io/ACME_LTDA_FRONT/
```

## Instruções para instalação Local

### Pré-requisitos

-  Python 3.8.8 ou versão superior instalado em seu sistema.


### Passo 1: Clonar o Repositório
```
git clone https://github.com/Daniel02md/ACME_LTDA.git
```

### Passo 2: Configurar o Ambiente Virtual e Instalar as Dependências

- Navegue até o diretório raiz do projeto clonado.
- Crie um ambiente virtual e ative-o. Dependendo do seu sistema operacional, execute os comandos adequados:

#### Variáveis de Ambiente obrigatórias

- `FLASK_ENV`: O ambiente de execução para a aplicação. As opções disponíveis são:

- `development`: Ambiente de desenvolvimento. (Padrão)
- `production`: Ambiente de produção. 
- `DEVELOPMENT_DATABASE_URI`: O link para o banco de dados no ambiente de desenvolvimento.
- `PRODUCTION_DATABASE_URI`: O link para o banco de dados no ambiente de produção. 
<br>

**Exemplo de links**

```
mysql+driver://user+password@host:port/DATABASE_NAME
```

#### Instale as dependências do projeto executando o seguinte comando:

```
python3 -m pip install -r requirements.txt
```

### Passo 3: Faça as migrações para o banco de dados

#### Comandos para executar uma migração:
```
flask --app migrate.py alembic upgrade
```

### Passo 4: Executar a Aplicação

- Após a conclusão da instalação das dependências, execute o seguinte comando para iniciar a aplicação:
```
python3 run.py
```

## API Rest - Endpoints

Base URL: `https://acmeltda-production.up.railway.app/`

### Criação de Funcionário

**Método:** `POST` 
<br>
**Endpoint:** `/funcionario`

Este endpoint permite criar um novo funcionário no sistema.

**Parâmetros de Requisição:**

Os parâmetros da requisição devem ser enviados no corpo da requisição como um formulário HTTP.

- `cpf` (string): O CPF do funcionário.
- `nome` (string): O nome do funcionário.
- `cargo` (string): O cargo do funcionário.
- `salário` (double): O salário do funcionário.

**Resposa de sucesso:**

```
{
  "status": "success",
  "success": {
    "code": 201,
    "message": "Successfully created"
  }
}
```
## Obter Funcionário por ID

**Método:** `GET`
**Endpoint:** `/funcionario/<int:id>`

Este endpoint permite obter os detalhes de um funcionário com base no seu ID.

**Parâmetros de Requisição:**

- `id` (inteiro): O ID do funcionário a ser obtido.

```
{
    "status": "success",
    "success": {
        "code": 200,
        "results": [
            [
                {
                    "CPF": "XXXXX",
                    "ID": 10,
                    "cargo": "Trainee Analista de Requisitos",
                    "nome": "XXXXX",
                    "salario": 1800.0
                }
            ]
        ]
    }
}
```

## Consulta de Funcionários

**Método:** `GET`
**Endpoint:** `/funcionario`

Este endpoint permite consultar todos os funcionários cadastrados no sistema. Retorna os valores em ordem alfabética.

**Parâmetros de Requisição:**

Nenhum parâmetro de requisição é necessário.

**Resposta de Sucesso:**

```
{
    "status": "success",
    "success": {
        "code": 200,
        "results": [
            [
                {
                    "CPF": "XXXXX",
                    "ID": 10,
                    "cargo": "Trainee Analista de Requisitos",
                    "nome": "XXXXX",
                    "salario": 1800.0
                }
            ]
        ]
    }
}
```
## Atualização de Funcionário

**Método:** `POST`
**Endpoint:** `/funcionario/<int:id>`

Este endpoint permite atualizar os dados de um funcionário existente com base no seu ID.

**Parâmetros de Requisição:**

- `id` (inteiro): O ID do funcionário a ser atualizado.
- Os dados atualizados do funcionário devem ser enviados no corpo da requisição como um formulário HTTP.

**Exemplo de Requisição:**

```http
POST /funcionario/1
Content-Type: application/x-www-form-urlencoded

nome=João+da+Silva&cargo=Desenvolvedor&salário=5500.0
```


**Resposta de sucesso:**
```
{
  "status": "success",
  "success": {
    "code": 200,
    "message": "Successfully updated"
  }
}
```
## Exclusão de Funcionário

**Método:** `DELETE`
**Endpoint:** `/funcionario/<int:id>`

Este endpoint permite excluir um funcionário existente com base no seu ID.

**Parâmetros de Requisição:**

- `id` (inteiro): O ID do funcionário a ser excluído.

