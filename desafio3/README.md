# Desafio 3 - Docker Compose Orquestrando Serviços

## Descrição
Aplicação composta por 3 serviços orquestrados via Docker Compose:
1. **Web**: Aplicação Flask que conta acessos.
2. **Redis**: Cache para armazenar o contador de acessos.
3. **DB**: Banco PostgreSQL (apenas instanciado para demonstrar dependência).

## Como executar
```bash
docker-compose up -d
```

## Testar
Acesse: http://localhost:5000
Recarregue a página para ver o contador aumentar.

## Parar
```bash
docker-compose down
```
