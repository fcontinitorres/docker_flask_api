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
    - Unprocessable Entity: 422 se não passar em alguma validação - Obs: Sem nenhum corpo.
DELETE /pessoa/<int:id>: Exclui uma pessoa pelo ID.
GET /estatisticas: Retorna estatísticas sobre as pessoas cadastradas.

Regras de Negócio
1. Cada pessoa deve ter um nome e uma idade.
2. A idade deve ser um número inteiro positivo.
3. O nome deve ser uma string não vazia.
"""

# From framework flask, import Flask class
from flask import Flask, jsonify, request
from jinja2.utils import markupsafe

# Create an instance of Flask class. __name__ is a special variable in Python that holds the name of the current module. 
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


lista_pessoas = [
    {"id": 1, "nome": "Felipe", "idade": 30},
    {"id": 2, "nome": "Julia", "idade": 25}
]

@app.route('/')
def hello():
    return 'Hello, World!'

# Define a route for the endpoint /pessoas that accepts GET requests
@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    return jsonify(lista_pessoas)

# Define a route for the endpoint /pessoa that accepts POST 
# Body: {"id": 3, "nome": "Maria", "idade": 28 }
@app.route('/pessoa', methods=['POST'])
def criar_pessoa():
    pessoa = request.json
    
    # Verificar se o JSON tem exatamente as chaves 'id', 'nome', 'idade'
    required_keys = {'id', 'nome', 'idade'}
    if set(pessoa.keys()) != required_keys:
        return '', 422
    
    # Verificar se id é um inteiro
    if not isinstance(pessoa['id'], int):
        return '', 422
    
    # Verificar se nome é uma string não vazia
    if not isinstance(pessoa['nome'], str) or not pessoa['nome'].strip():
        return '', 422
    
    # Verifica se a idade é um valor positivo
    if pessoa["idade"] <= 0:
        return '', 422

    lista_pessoas.append(pessoa)
    return jsonify( mensagem = 'Pessoa cadastrada', lista_de_pessoas = lista_pessoas), 201

@app.route('/pessoa/<int:id>', methods=['DELETE'])
def excluir_pessoa(id):
    for pessoa in lista_pessoas:
        if pessoa['id'] == id:
            lista_pessoas.remove(pessoa)
            return jsonify(mensagem = 'Pessoa excluída', lista_de_pessoas = lista_pessoas), 200
    return jsonify(mensagem = 'Pessoa não encontrada'), 404

# Running the application. Making it available.
if __name__ == '__main__':
    # Run the application on all available network interfaces
    app.run(host='0.0.0.0', port=5002)
