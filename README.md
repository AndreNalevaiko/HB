# LEIA ANTES DE QUALQUER COISA

Esse arquivo deve conter informações úteis para esse sistema.

Não adicione aqui o que pode ser considerado um procedimento em comum para outros sistemas.

Leia primeiro a nossa diretriz de gerenciamento de conhecimento.

## Desenvolvimento

### Inciando o virtualenv

```
virtualenv -p /usr/bin/python3 ~/.virtualenvs/gorillassite
source ~/.virtualenvs/gorillassite/bin/activate
pip install -r requirements.txt
```

### Rodando localmente

```
source ~/.virtualenvs/gorillassite/bin/activate

python3 run.py
```

### Commits locais

Para adicionar o que foi alterado utilize

```
git add .
git commit
```

**ATENÇÃO: Sempre envie um comentário.**

## Implantação

### Build & Push

Esses comandos definem como se builda uma imagem e manda para o registry da Gorillas.

#### Staging Version (Development)

```
docker login docker.gorillascode.com
make push_develop
```

### Release Version (Production)

1. Criar uma nova release usando o [git-flow](http://danielkummer.github.io/git-flow-cheatsheet/)
1. Atualizar `APP_VERSION` no arquivo `config.py`
1. Atualizar `VERSION` no arquivo `Makefile`
1. Comitar as alterações referenciando a release a ser criada.
1. Finalizar a release
1. Executar os comandos abaixo:

```
make push
```

### Deploy

Esses comando devem ser rodados dentro do projeto `gorillas-compose`.

#### Staging Version (Development)

```
docker-compose -f landing-page.yml -f env-staging.yml pull landing_page
docker-compose -f landing-page.yml -f env-staging.yml up -d landing_page
```

### Run

```
docker run -d -e GORILLASSITE_LOGGING_CONFIG=logging.yaml -e GORILLASSITE_FLASK_CONFIG=gorillassite.config.Production --restart="unless-stopped" --name=gorillassite1 gorillas/gorillassite:latest
```

### Accessing

```
docker exec -it landing-page /bin/bash
```
