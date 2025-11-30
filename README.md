# Projeto FCCPD - Desafios Docker e Microserviços

Este repositório contém as soluções para os desafios propostos.

## Estrutura

- `/desafio1` - Containers em Rede (Implementado)
- `/desafio2` - Volumes e Persistência (Implementado)
- `/desafio3` - Docker Compose Orquestrando Serviços (Implementado)
- `/desafio4` - Microsserviços Independentes (Implementado)
- `/desafio5` - Microsserviços com API Gateway (Implementado)

## Arquitetura Geral e Soluções

Este projeto explora conceitos fundamentais de Docker e arquitetura de microsserviços através de desafios práticos.

- **Desafio 1 (Containers em Rede):** Demonstra a comunicação entre múltiplos containers Docker em uma rede isolada.
- **Desafio 2 (Volumes e Persistência):** Aborda a utilização de volumes para persistir dados gerados por containers, garantindo que as informações não sejam perdidas após a destruição do container.
- **Desafio 3 (Docker Compose Orquestrando Serviços):** Introduz o Docker Compose como ferramenta para definir e gerenciar aplicações multi-container, simplificando a orquestração de serviços.
- **Desafio 4 (Microsserviços Independentes):** Foca na implementação de microsserviços que operam de forma independente, comunicando-se entre si, mas sem a camada de orquestração do compose para simular um ambiente de cluster.
- **Desafio 5 (Microsserviços com API Gateway):** Expande o conceito de microsserviços, adicionando um API Gateway para centralizar o roteamento de requisições e proteger os serviços de backend.

Cada pasta contém seu próprio `README.md` com instruções específicas de execução.

## Como navegar

Para testar um desafio, entre na pasta correspondente e siga as instruções do README local.

Exemplo:
```bash
cd desafio1
cat README.md
```
