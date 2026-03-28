# docker_flask_api
Flask Docker API - Uma API simples em Python usando Flask, containerizada com Docker e Docker Compose.

## Descrição Projeto

Este projeto é uma API simples em Python usando Flask, empacotada em Docker. Ele serve como exemplo de uma aplicação pequena e funcional, com endpoints para gerenciar pessoas em memória.

### Arquitetura

- Arquitetura monolítica simples
- Toda a lógica está em um único serviço/API (`main.py`)
- Não há banco de dados externo; os dados são armazenados em uma lista Python em memória
- Adequado para projetos de demonstração, protótipos e APIs pequenas

### Funcionalidades

- `GET /pessoas`: retorna a lista de pessoas cadastradas
- `POST /pessoa`: cadastra uma nova pessoa com `id`, `nome` e `idade`
- `DELETE /pessoa/<id>`: remove uma pessoa pelo identificador

### Como funciona o código

- `main.py` cria a aplicação Flask e define os endpoints
- A lista `lista_pessoas` mantém os registros em memória
- O `POST /pessoa` valida os dados antes de adicionar uma pessoa
- O `DELETE /pessoa/<id>` busca e elimina o registro correspondente

### Ferramentas e tecnologias

- Flask 3.x: framework web para Python
- Docker: empacotamento da aplicação em contêiner

### Comandos DockerFile

- docker build . -t "nome_imagem"
    > Criar uma imagem a partir do dockerFile

- docker run --name="nome_imagem" -p=3000:5002 "nome_container"
    > Criando o container a partir da imagem

- docker start "nome_ou_id_container"
    > Inicializando um container já criado

- docker stop "nome_ou_id_container"
    > Parando um container inicializado

- Exetar o docker compose
    > docker compose up
