#!/bin/bash
cd "$(dirname "$0")"

# Build
docker build -t app-persistente ./app

# Criar volume
docker volume create dados-desafio2

# Rodar primeira vez
echo "--- Execução 1 ---"
docker run --rm -v dados-desafio2:/data app-persistente

# Rodar segunda vez (deve mostrar persistência)
echo "--- Execução 2 (Após remover container) ---"
docker run --rm -v dados-desafio2:/data app-persistente
