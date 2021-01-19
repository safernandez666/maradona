# Maradona BOT 

3-tier application to be able to build with Docker-Compose or with Kubernetes.

The application is a Telegam Bot, with phrases by Maradona.


## Docker Compose Way

#### Build the Image

```bash
docker-compose build
```

#### Run the Container

```bash
docker-compose up
```

## The Kubernetes Way

You must update **02-maradona-secrets.yaml** with your secrets.

TOKEN_TELEGRAM
CHAT_ID
MYSQL_ROOT_PASSWORD

On kubernetes folder:

```bash
kubectl apply -f ./
```

Surely the code can be improved. Adding limits to the manifestos, the idea was to play with both ways. I hope it helps you.