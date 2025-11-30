#!/bin/bash
cd "$(dirname "$0")"

# Criar rede
docker network create rede-desafio1

# Build das imagens
docker build -t servidor-img ./server
docker build -t cliente-img ./client

# Rodar containers na rede
docker run -d --name server --network rede-desafio1 servidor-img
docker run -d --name client --network rede-desafio1 cliente-img

# Mostrar logs
echo "Aguardando logs..."
sleep 5
docker logs client
