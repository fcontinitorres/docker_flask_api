import pytest
from main import app, lista_pessoas

class TestMainUnit:
    """Testes unitários para as funções da API"""

    def setup_method(self):
        """Reinicia a lista de pessoas antes de cada teste"""
        global lista_pessoas
        lista_pessoas = [
            {"id": 1, "nome": "Felipe", "idade": 30},
            {"id": 2, "nome": "Julia", "idade": 25}
        ]

    def test_get_pessoas(self):
        """Testa a função get_pessoas"""
        with app.test_client() as client:
            response = client.get('/pessoas')
            assert response.status_code == 200
            data = response.get_json()
            assert isinstance(data, list)
            assert len(data) == 2
            assert data[0]['nome'] == 'Felipe'

    def test_criar_pessoa_sucesso(self):
        """Testa criação de pessoa com dados válidos"""
        with app.test_client() as client:
            pessoa_data = {"id": 3, "nome": "Maria", "idade": 28}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 201
            data = response.get_json()
            assert data['mensagem'] == 'Pessoa cadastrada'
            assert len(data['lista_de_pessoas']) == 3

    def test_criar_pessoa_chaves_invalidas(self):
        """Testa criação com chaves extras ou faltando"""
        with app.test_client() as client:
            # Chaves extras
            pessoa_data = {"id": 3, "nome": "Maria", "idade": 28, "extra": "campo"}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

            # Chaves faltando
            pessoa_data = {"id": 3, "nome": "Maria"}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

    def test_criar_pessoa_id_invalido(self):
        """Testa criação com id não inteiro"""
        with app.test_client() as client:
            pessoa_data = {"id": "3", "nome": "Maria", "idade": 28}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

    def test_criar_pessoa_nome_invalido(self):
        """Testa criação com nome inválido"""
        with app.test_client() as client:
            # Nome vazio
            pessoa_data = {"id": 3, "nome": "", "idade": 28}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

            # Nome apenas espaços
            pessoa_data = {"id": 3, "nome": "   ", "idade": 28}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

            # Nome não string
            pessoa_data = {"id": 3, "nome": 123, "idade": 28}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

    def test_criar_pessoa_idade_invalida(self):
        """Testa criação com idade inválida"""
        with app.test_client() as client:
            # Idade não positiva
            pessoa_data = {"id": 3, "nome": "Maria", "idade": 0}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

            pessoa_data = {"id": 3, "nome": "Maria", "idade": -5}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

            # Idade não inteiro
            pessoa_data = {"id": 3, "nome": "Maria", "idade": "28"}
            response = client.post('/pessoa', json=pessoa_data)
            assert response.status_code == 422

    def test_excluir_pessoa_sucesso(self):
        """Testa exclusão de pessoa existente"""
        with app.test_client() as client:
            response = client.delete('/pessoa/1')
            assert response.status_code == 200
            data = response.get_json()
            assert data['mensagem'] == 'Pessoa excluída'
            assert len(data['lista_de_pessoas']) == 1

    def test_excluir_pessoa_inexistente(self):
        """Testa exclusão de pessoa inexistente"""
        with app.test_client() as client:
            response = client.delete('/pessoa/999')
            assert response.status_code == 404
            data = response.get_json()
            assert data['mensagem'] == 'Pessoa não encontrada'