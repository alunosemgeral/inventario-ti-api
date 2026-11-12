# Guia rápido do professor

## Ordem sugerida de merges

- Fase 1: TASK-01, TASK-02, TASK-03, TASK-12 (arquivos independentes).
- Fase 2: TASK-04, TASK-05, TASK-06, TASK-07, TASK-08 (CRUD; integração após dependências).
- Fase 3: TASK-09, TASK-10, TASK-11 (filtros e estatísticas).

## ClickUp

Crie uma List `Inventário de TI`, com status `BACKLOG`, `TODO`, `DOING`, `IN REVIEW`, `DONE`. Cadastre as 12 tarefas com título igual ao arquivo TASK-XX; cole a descrição do arquivo correspondente, atribua um aluno e use `IN REVIEW` para Pull Requests aguardando aprovação.

## Recomendações

- Cada estudante altera apenas seu arquivo.
- Faça merge das dependências primeiro.
- Antes de aceitar uma task, execute a API e teste o endpoint.
- Faça o merge de um PR por vez; peça atualização da branch se houver conflitos.
- O endpoint `/health` já está funcional; todos os demais retornam 501 até a implementação.
