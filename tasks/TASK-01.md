# TASK-01 — Modelos de dados

**Responsável:** aluno designado pelo professor  
**Arquivo exclusivo:** `app/models/equipment.py`  
**Dependências:** Nenhum; primeira integração.

## Passo a passo no VS Code

1. Faça `git switch main` e `git pull origin main`.
2. Crie uma branch: `git switch -c task-01-equipment`.
3. Abra o arquivo `app/models/equipment.py` no VS Code.
4. Leia os comentários `TODO` e implemente a atividade abaixo.
5. Salve e execute os testes indicados.
6. Registre no ClickUp o que fez, o resultado e eventual impedimento.
7. Faça `git add app/models/equipment.py` e `git commit -m "feat: modelos de dados"`.
8. Execute `git push -u origin NOME-DA-SUA-BRANCH` e abra um Pull Request no GitHub.

## O que implementar

Crie classes Pydantic `EquipmentCreate`, `EquipmentUpdate` e `Equipment`. Use `name: str`, `category: str`, `status: str = "available"`; em `EquipmentUpdate`, campos opcionais com `None`; em `Equipment`, adicione `id: int`. Use `Field(min_length=1)` em name e category.

## Como validar

Execute `python -c "from app.models.equipment import EquipmentCreate; print(EquipmentCreate(name='PC 01',category='desktop'))"`.

> Para iniciar a API: `python -m uvicorn app.main:app --reload`. Teste pelo Postman em `http://127.0.0.1:8000`.

## Critérios de aceitação

- O código está no arquivo indicado, com nomes de funções claros.
- O cenário positivo funciona.
- O cenário de erro indicado, quando aplicável, foi verificado.
- O aluno registrou evidência no ClickUp e abriu um Pull Request.

## Atenção

Não edite `app/main.py` nem arquivos de colegas. Caso a tarefa dependa de código ainda não integrado, registre o bloqueio e aguarde orientação do professor.
