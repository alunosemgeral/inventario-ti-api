# TASK-12 — Função de resumo

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/services/summary.py`  
**Dependências:** Nenhum; integrar antes da TASK-11

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-12-summary`.
3. Abra o arquivo `app/services/summary.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/services/summary.py` e `git commit -m "feat: função de resumo"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Implemente `count_by_status(items: list[dict]) -> dict[str,int]` com chaves available, maintenance e borrowed iniciadas em zero. Percorra os itens e incremente o contador do status correspondente. Ignore status desconhecidos.

## Como validar

Teste com lista de 3 equipamentos (2 available, 1 maintenance) e confirme {"available":2,"maintenance":1,"borrowed":0}.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
