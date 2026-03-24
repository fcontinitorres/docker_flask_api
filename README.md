# docker_flask_api
Flask Docker API - Uma API simples em Python usando Flask, containerizada com Docker e Docker Compose.

Comandos DockerFile

Criar uma iamgem a partir do dockerFile
- docker build . -t "nome_imagem"

Criando o container a partir da imagem
- docker run --name="nome_imagem" -p=3000:5002 "nome_container"

Inicializando um container já criado
- docker start 92ff467b49f05f1d38b398747729d20813fa5c3578d397299f45da05f219aeba

Parando um container inicializado
- docker stop 92ff467b49f05f1d38b398747729d20813fa5c3578d397299f45da05f219aeba
