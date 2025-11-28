# Projeto FCCPD - Microserviços com Docker

Projeto implementando microserviços com Docker Compose, API Gateway e balanceamento de carga.

## Arquitetura

- **3 instâncias backend** (FastAPI) executando microserviços
- **API Gateway** (Nginx) para roteamento e balanceamento de carga
- **Volumes persistentes** para logs e dados
- **Rede isolada** para comunicação entre containers

## Microserviços

- `/users` - Gerenciamento de usuários
- `/products` - Gerenciamento de produtos
- `/orders` - Gerenciamento de pedidos
- `/payments` - Gerenciamento de pagamentos

## Comandos

### Iniciar todos os serviços
```bash
docker-compose up -d
```

### Parar todos os serviços
```bash
docker-compose down
```

### Ver logs
```bash
docker-compose logs -f
```

### Ver logs de instância específica
```bash
docker-compose logs -f backend1
docker-compose logs -f backend2
docker-compose logs -f backend3
docker-compose logs -f gateway
```

### Rebuild
```bash
docker-compose up -d --build
```

## Testar

### API Gateway
```bash
curl http://localhost:8080/
```

### Microserviços
```bash
curl http://localhost:8080/users
curl http://localhost:8080/products
curl http://localhost:8080/orders
curl http://localhost:8080/payments
```

## Estrutura

```
.
├── backend/
│   ├── cliente.py
│   ├── Dockerfile
│   └── requirements.txt
├── reverse_proxy/
│   ├── nginx.conf
│   └── Dockerfile
└── docker-compose.yml
```

## Volumes

- `logs` - Armazena logs das aplicações
- `data` - Armazena dados persistentes

## Rede

Todos os containers comunicam através da rede `app-network` (bridge).
