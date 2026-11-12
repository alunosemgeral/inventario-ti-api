# TASK-03 — Validações de negócio

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/services/validators.py`  
**Dependências:** Nenhum; primeira integração.

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-03-validators`.
3. Abra o arquivo `app/services/validators.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/services/validators.py` e `git commit -m "feat: validações de negócio"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Implemente `normalize_name(name)` removendo espaços nas pontas e rejeitando vazio com `ValueError`. Implemente `validate_status(status)` convertendo para minúsculas e aceitando somente available, maintenance, borrowed; em caso contrário, `ValueError`.

## Como validar

Teste funções no Python com entradas válidas e inválidas.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
