# Desafio 2 - Volumes e Persistência

## Descrição
Demonstração de persistência de dados usando Docker Volumes.
Um script Python insere um registro em um banco SQLite localizado em um volume montado.
A cada execução, o histórico de registros aumenta, provando que os dados sobrevivem à destruição do container.

## Como executar
```bash
chmod +x run.sh
./run.sh
```

## Limpeza
```bash
docker volume rm dados-desafio2
```
