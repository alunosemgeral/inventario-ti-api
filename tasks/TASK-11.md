# TASK-11 — Endpoint de estatísticas

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/routers/statistics.py`  
**Dependências:** TASK-02, TASK-12

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-11-statistics`.
3. Abra o arquivo `app/routers/statistics.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/routers/statistics.py` e `git commit -m "feat: endpoint de estatísticas"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Importe `store` e `count_by_status` de `app.services.summary`. Busque itens com `store.list_equipments()`, calcule o resumo e retorne {"total": len(items), "by_status": resumo}.

## Como validar

GET /equipments/statistics; espere total e contagens por status.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
