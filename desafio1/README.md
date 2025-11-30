# Desafio 1 - Containers em Rede

## Descrição
Dois containers conectados por uma rede bridge customizada (`rede-desafio1`).
- **Server**: Python HTTP Server na porta 8080.
- **Client**: Container Alpine rodando `curl` em loop.

## Como executar
```bash
chmod +x run.sh
./run.sh
```

## Limpeza
```bash
docker rm -f server client
docker network rm rede-desafio1
```
