# docker_flask_api
Flask Docker API - Uma API simples em Python usando Flask, containerizada com Docker e Docker Compose.

## Descrição Projeto


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

### Terminal Commands
#### Teste API no terminal
> curl -X POST http://localhost:3000/pessoa
> curl -X POST http://localhost:3000/pessoa -H "Content-Type: application/json" -d '{"nome": "João", "idade": 30}'

Obs: Nunca usar aspas simples na criação de um json!