# Chamados ADS

## Estudante

Everton Lucas Fernandes - Matricula 2025017020

## Objetivo do projeto

Este projeto disponibiliza uma API simples para indicar que o serviço de chamados está ativo e em funcionamento.

## Instalação das dependências

Na pasta do projeto, instale as dependências a partir do arquivo de lock:

```bash
uv sync --locked
```

## Execução da aplicação

Execute o servidor Flask:

```bash
uv run flask --app app run
```

## Acesso à aplicação

Com o servidor em execução, acesse:

```text
http://127.0.0.1:5000/
```

A rota inicial (`/`) deve retornar a seguinte resposta JSON:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```
