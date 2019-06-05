# Projetos UFSC
:page_with_curl: projeto para facilitar o acesso a dados abertos da UFSC

![Em desenvolvimento](https://img.shields.io/badge/initial%20version-in--progress-brightgreen.svg)

O objetivo desse projeto é levar informação para a população, utilizando dados públicos de projetos da UFSC para que a informação esteja acessível a todos.

Acesso a dados abertos UFSC: http://transparencia.proex.ufsc.br/

## Iniciando migração dos dados
```
// ./research/utils/.env

MONGODB_URL="mongodb://<user>:<password>@<db_url>:<port>/<database>"
```

### Instalação via Docker

Na pasta ./research
```
    docker-compose up
```

### Usando com docker

Na pasta ./research
```
    docker-compose exec web py fetch:funders
```
e
```
    docker-compose exec web py fetch:departments
```
e
```
    docker-compose exec web py fetch:projects
```