# TASK-10 — Filtro por status

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/routers/filter_status.py`  
**Dependências:** TASK-02, TASK-03, TASK-04

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-10-filter_status`.
3. Abra o arquivo `app/routers/filter_status.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/routers/filter_status.py` e `git commit -m "feat: filtro por status"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Valide o parâmetro `status` com `validate_status`, convertendo ValueError em HTTP 422. Filtre `store.list_equipments()` pelo status validado.

## Como validar

GET /equipments/filter/status?status=maintenance; teste também status inválido (422).

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
