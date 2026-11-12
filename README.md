# Inventário de TI — API REST (Projeto Didático)

Projeto colaborativo da disciplina **Análise e Projetos de Sistemas**, do curso Técnico em Desenvolvimento de Sistemas. O professor atua como líder técnico e 12 estudantes implementam tarefas individuais usando **GitHub, ClickUp, VS Code e Postman**.

> **Estado inicial:** estrutura executável, com endpoints ainda não implementados (HTTP 501). Cada tarefa deve ser desenvolvida pelos alunos. O endpoint `/health` já funciona.

## Objetivo

Construir uma API para gerenciar equipamentos de informática de uma escola, praticando requisitos, planejamento, versionamento, revisão de código, integração e testes HTTP.

## Tecnologias

- Python 3.11 ou superior
- FastAPI (API REST)
- Uvicorn (servidor local)
- Pydantic (validação e modelos de dados)
- Postman (testes manuais)
- Git/GitHub (branches e Pull Requests)
- ClickUp (backlog e acompanhamento)
- VS Code (editor)

**Armazenamento:** dicionário Python em memória; os dados são perdidos ao reiniciar a aplicação. Não há autenticação nem banco de dados nesta primeira versão.

## Funcionalidades planejadas

| Método | Endpoint | Função | Responsável |
|---|---|---|---|
| GET | `/health` | Verificar disponibilidade | Professor (pronto) |
| POST | `/equipments` | Cadastrar equipamento | TASK-04 |
| GET | `/equipments` | Listar equipamentos | TASK-05 |
| GET | `/equipments/{equipment_id}` | Consultar por ID | TASK-06 |
| PUT | `/equipments/{equipment_id}` | Atualizar equipamento | TASK-07 |
| DELETE | `/equipments/{equipment_id}` | Excluir equipamento | TASK-08 |
| GET | `/equipments/filter/category?category=notebook` | Filtrar por categoria | TASK-09 |
| GET | `/equipments/filter/status?status=maintenance` | Filtrar por status | TASK-10 |
| GET | `/equipments/statistics` | Resumo por status | TASK-11 + TASK-12 |

### Exemplo de equipamento

```json
{
  "id": 1,
  "name": "Notebook Dell",
  "category": "notebook",
  "status": "available"
}
```

Status permitidos: `available`, `maintenance`, `borrowed`.

## Como executar

1. Faça o clone e entre na pasta:

   ```bash
   git clone https://github.com/SEU-USUARIO/inventario-ti-api.git
   cd inventario-ti-api
   ```

2. Crie e ative o ambiente virtual:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux/macOS**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências e execute:

   ```bash
   python -m pip install -r requirements.txt
   python -m uvicorn app.main:app --reload
   ```

4. Acesse `http://127.0.0.1:8000/health` (resposta esperada: `{"status":"ok"}`). Documentação interativa: `http://127.0.0.1:8000/docs`.

5. Abra o Postman e envie as requisições. **Antes de implementar cada task, os endpoints correspondentes retornam HTTP 501**.

## Fluxo de colaboração

Cada estudante recebe uma tarefa do ClickUp e trabalha **somente no(s) arquivo(s) designado(s)**, salvo autorização do professor.

```bash
# Após clonar, atualizar a main local:
git switch main
git pull origin main

# Criar branch para sua tarefa:
git switch -c task-04-cadastro

# Depois de editar e testar:
git status
git add app/routers/create.py
git commit -m "feat: implement equipment creation"
git push -u origin task-04-cadastro
```

No GitHub, abra um **Pull Request** da sua branch para `main`. O professor revisa e faz o merge. **Não envie push direto para main.**

> Quando uma tarefa depender de outra ainda não integrada, espere o merge da dependência e atualize a branch. Evite alterações simultâneas nos mesmos arquivos.

## Ordem de integração recomendada

1. TASK-01 (modelos), TASK-02 (repositório) e TASK-03 (validações).
2. TASK-04 a TASK-08 (CRUD).
3. TASK-09 e TASK-10 (filtros).
4. TASK-12 (função de resumo) e TASK-11 (endpoint de estatísticas).

As tarefas são distribuídas desde o início, mas **não precisam ser integradas simultaneamente**. Cada estudante pode preparar seu código e aguardar dependências.

## Estrutura do projeto

```text
app/
  main.py                  # Aplicação e registro das rotas (professor)
  models/equipment.py      # TASK-01
  repositories/store.py    # TASK-02
  services/validators.py   # TASK-03
  services/summary.py      # TASK-12
  routers/create.py        # TASK-04
  routers/list_all.py      # TASK-05
  routers/get_by_id.py     # TASK-06
  routers/update.py        # TASK-07
  routers/delete.py        # TASK-08
  routers/filter_category.py # TASK-09
  routers/filter_status.py   # TASK-10
  routers/statistics.py    # TASK-11
tasks/                      # Instruções detalhadas para os 12 alunos
postman/                    # Requisições de teste
requirements.txt
```

## Critérios de conclusão

Uma tarefa está pronta quando: código implementado, endpoint ou função testado, evidências anexadas no ClickUp, commit enviado para a branch e Pull Request aberto. O professor move a tarefa para DONE após revisão e merge.

## Regras de convivência no repositório

- Não editar arquivos de outros alunos sem alinhamento.
- Não enviar senhas, tokens, `.env` ou `.venv` ao GitHub.
- Usar nomes de branches como `task-01-modelos`.
- Informar impedimentos e dependências no ClickUp.
- Manter comentários e nomes de código em inglês; explicações em sala podem ser em português.

## Licença

Projeto educacional. Defina uma licença com a turma antes de permitir reutilização pública.
