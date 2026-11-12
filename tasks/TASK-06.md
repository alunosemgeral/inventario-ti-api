# TASK-06 — Consulta por ID

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/routers/get_by_id.py`  
**Dependências:** TASK-02, TASK-04

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-06-get_by_id`.
3. Abra o arquivo `app/routers/get_by_id.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/routers/get_by_id.py` e `git commit -m "feat: consulta por id"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Use `store.find_equipment(equipment_id)`; se não existir, lance `HTTPException(status_code=404, detail="Equipment not found")`; senão, retorne o registro.

## Como validar

GET /equipments/1 e GET /equipments/999; espere 200 ou 404.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
