# TASK-04 — Endpoint de cadastro

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/routers/create.py`  
**Dependências:** TASK-01, TASK-02, TASK-03

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-04-create`.
3. Abra o arquivo `app/routers/create.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/routers/create.py` e `git commit -m "feat: endpoint de cadastro"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Substitua o parâmetro `payload: dict` por `payload: EquipmentCreate`. Valide nome e status usando `validators`, converta o modelo com `model_dump()`, chame `store.add_equipment(...)` e retorne o registro. Configure `status_code=201` no decorator; transforme ValueError em HTTP 422.

## Como validar

POST /equipments com JSON {"name":"Notebook Dell","category":"notebook","status":"available"}; espere 201 e id.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
