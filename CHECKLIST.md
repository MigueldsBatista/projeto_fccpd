# Checklist de Requisitos do Projeto

## ✅ Desafio 1 - Containers em Rede

### Requisito: Comunicação entre múltiplos containers em rede Docker
- ✅ **Implementado em:** `docker-compose.yml` (linhas 51-53)
  - Rede `app-network` com driver bridge
  - 4 containers conectados: backend1, backend2, backend3, gateway

### Requisito: Uso de docker-compose para orquestração
- ✅ **Implementado em:** `docker-compose.yml`
  - Define 4 serviços (3 backends + 1 gateway)
  - Gerencia dependências com `depends_on`

### Requisito: Containers devem se comunicar pelo nome
- ✅ **Implementado em:** `reverse_proxy/nginx.conf` (linhas 7-27)
  - Upstream usa nomes: `backend1:8000`, `backend2:8000`, `backend3:8000`

---

## ✅ Desafio 2 - Volumes e Persistência

### Requisito: Volumes nomeados para persistência de dados
- ✅ **Implementado em:** `docker-compose.yml` (linhas 47-49)
  - Volume `logs` para logs da aplicação
  - Volume `data` para dados persistentes

### Requisito: Múltiplos containers compartilhando volumes
- ✅ **Implementado em:** `docker-compose.yml` (linhas 10-11, 20-21, 30-31)
  - Todos os 3 backends compartilham os mesmos volumes `logs` e `data`
  - Path: `/app/logs` e `/app/data`

### Requisito: Dados persistem após restart dos containers
- ✅ **Implementado:** Volumes são externos ao ciclo de vida dos containers
  - `docker-compose down` não remove volumes
  - Dados preservados entre restarts

---

## ✅ Desafio 3 - Docker Compose Orquestrando Serviços

### Requisito: 3+ containers backend rodando simultaneamente
- ✅ **Implementado em:** `docker-compose.yml` (linhas 4-34)
  - `backend1` (INSTANCE_ID=1)
  - `backend2` (INSTANCE_ID=2)
  - `backend3` (INSTANCE_ID=3)

### Requisito: 1 container de reverse proxy (Nginx)
- ✅ **Implementado em:** `docker-compose.yml` (linhas 36-44)
  - Service `gateway` com Nginx
  - Porta exposta: 8080

### Requisito: Balanceamento de carga entre backends
- ✅ **Implementado em:** `reverse_proxy/nginx.conf` (linhas 7-27)
  - 4 upstreams configurados (users, products, orders, payments)
  - Cada upstream distribui para backend1, backend2, backend3
  - Algoritmo: round-robin (padrão)

---

## ✅ Desafio 4 - Microserviços Independentes

### Requisito: Diferentes serviços com responsabilidades isoladas
- ✅ **Implementado em:** `backend/cliente.py`
  - `/users` (linhas 13-15) - Gerenciamento de usuários

### Requisito: Cada microserviço executando em container separado
- ✅ **Implementado:** 3 instâncias backend processam todos os microserviços
  - Identificação via `INSTANCE_ID` na resposta
  - Load balancing distribui requests entre instâncias

### Requisito: Comunicação via API
- ✅ **Implementado:** FastAPI expondo endpoints REST
  - Formato: JSON
  - HTTP GET requests

---

## ✅ Desafio 5 - Microserviços com API Gateway

### Requisito: API Gateway centralizado (Nginx)
- ✅ **Implementado em:** `reverse_proxy/nginx.conf` (linhas 29-62)
  - Nginx escutando porta 8080
  - Roteamento baseado em path

### Requisito: Roteamento de requisições para microserviços
- ✅ **Implementado em:** `reverse_proxy/nginx.conf`
  - `/users` → `backend_users` upstream

### Requisito: Load balancing
- ✅ **Implementado em:** `reverse_proxy/nginx.conf` (linhas 7-27)
  - Nginx distribui automaticamente (round-robin)
  - Logs mostram qual backend processou: `upstream: $upstream_addr`

### Requisito: Headers de proxy configurados
- ✅ **Implementado em:** `reverse_proxy/nginx.conf` (linhas 38-39, 44-45, 50-51, 56-57)
  - `Host`: $host
  - `X-Real-IP`: $remote_addr

---

## 📊 Recursos Adicionais Implementados

### Logging e Monitoramento
- ✅ **Nginx:** Log customizado mostrando upstream backend
  - Arquivo: `reverse_proxy/nginx.conf` (linhas 4-5)
  - Formato: timestamp, IP, request, upstream, status

### Identificação de Instâncias
- ✅ **Backend:** Variáveis de ambiente para identificação
  - `SERVICE_NAME` e `INSTANCE_ID`
  - Retornado em cada resposta JSON

### Documentação
- ✅ **README.md:** Instruções completas de uso
- ✅ **CHECKLIST.md:** Este arquivo

---

## 🧪 Comandos de Teste

### Iniciar ambiente completo
```bash
docker-compose up -d
```

### Testar load balancing (fazer múltiplas requisições)
```bash
for i in {1..9}; do curl http://localhost:8080/users; echo; done
```

### Ver logs do gateway (mostra qual backend processou)
```bash
docker-compose logs -f gateway
```

### Ver logs dos backends
```bash
docker-compose logs -f backend1 backend2 backend3
```

### Verificar volumes
```bash
docker volume ls | grep projeto_fccpd
```

### Inspecionar rede
```bash
docker network inspect projeto_fccpd_app-network
```

---

## 📁 Estrutura de Arquivos

```
projeto_fccpd/
├── backend/
│   ├── cliente.py          # Microserviços (4 endpoints)
│   ├── Dockerfile          # Imagem Python + FastAPI
│   └── requirements.txt    # Dependências
├── reverse_proxy/
│   ├── nginx.conf          # Config do API Gateway + Load Balancer
│   └── Dockerfile          # Imagem Nginx
├── docker-compose.yml      # Orquestração (3 backends + gateway)
├── README.md               # Documentação de uso
└── CHECKLIST.md            # Este arquivo
```

---

## ✅ Status Final

**Todos os 5 desafios implementados e funcionais:**
1. ✅ Containers em Rede
2. ✅ Volumes e Persistência  
3. ✅ Docker Compose Orquestrando
4. ✅ Microserviços Independentes
5. ✅ API Gateway com Load Balancing
