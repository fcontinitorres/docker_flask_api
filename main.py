# From framework flask, import Flask class
from flask import Flask
from jinja2.utils import markupsafe

# Create an instance of Flask class. __name__ is a special variable in Python that holds the name of the current module. 
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the application on all available network interfaces
    app.run(host='0.0.0.0', port=5002)

"""
Deifnicação da API

API REST para Gerenciamento de Pessoas
Vamos armazenar os dados em memória cache

Endpoint:
GET /pessoas: Retorna uma lista de pessoas.
POST /pessoa: Cria uma nova pessoa.
    Formato do corpo da requisição para criar uma pessoa:
    {
        "nome": "João",
        "idade": 30
    }
    Respostas:
    - Sucesso: 201 Createdo
    - Erro: 400 Bad Request - A API não entendeu a requisição
    - Unprocessable Entity: 422 se não passar em alguma validação - Obs: Sem nenhum corpo.
DELETE /pessoas/ Exclui uma pessoa pelo ID.
GET /estatisticas: Retorna estatísticas sobre as pessoas cadastradas.

Regras de Negócio
1. Cada pessoa deve ter um nome e uma idade.
2. A idade deve ser um número inteiro positivo.
3. O nome deve ser uma string não vazia.
"""


"""
@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    return 'Lista de pessoas'

# Running the application. Making it available.
app.run

"""

