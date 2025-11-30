# Desafio 5 - Microsserviços com API Gateway

## Arquitetura

Este projeto implementa uma arquitetura de microsserviços utilizando Docker Compose.

- **API Gateway (Nginx)**: Ponto único de entrada (Porta 8080). Roteia requisições para os serviços apropriados.
- **Service Users (FastAPI)**: Gerencia dados de usuários.
- **Service Orders (FastAPI)**: Gerencia dados de pedidos.

## Estrutura de Pastas

- `reverse_proxy/`: Configuração do Nginx (Gateway).
- `service_users/`: Código Python/FastAPI para o serviço de usuários.
- `service_orders/`: Código Python/FastAPI para o serviço de pedidos.

## Como Executar

1. Construir e iniciar os containers:
   ```bash
   docker-compose up -d --build
   ```

2. Testar os endpoints:
   - Usuários: `http://localhost:8080/users`
   - Pedidos: `http://localhost:8080/orders`

3. Parar a execução:
   ```bash
   docker-compose down
   ```
