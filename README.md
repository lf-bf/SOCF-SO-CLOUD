# Servidor Web Flask - Métricas do Sistema

Este projeto implementa um servidor web em Flask que exibe informações do sistema operacional.

## Integrantes da Equipe
Luiz Fernando Brasão e João Pedro Giovannoni

O servidor estará disponível em https://socf-so-cloud-3p6l.onrender.com

## Rotas Disponíveis

### `/info`
Retorna o nome dos integrantes da equipe.

### `/metricas`
Retorna as métricas do sistema em formato JSON.


## Módulos Utilizados

- `os`: Para obter informações do processo
- `platform`: Para detectar o sistema operacional
- `psutil`: Para obter métricas de CPU e memória
