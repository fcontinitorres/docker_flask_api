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
