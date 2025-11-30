# Desafio 4 - Microsserviços Independentes

## Descrição
Dois microsserviços independentes que se comunicam via HTTP.
- **Service A**: Retorna uma lista de usuários em JSON.
- **Service B**: Consome o Service A e exibe os dados formatados em HTML.

## Como executar
```bash
docker-compose up -d --build
```

## Testar
Acesse o Service B: http://localhost:5002
Você verá a lista de usuários obtida do Service A.

## Parar
```bash
docker-compose down
```
