from features import ver_tarefa, add_tarefa, edit_tarefa
from db import cria_tabela

cria_tabela()

while True:
    escolha = int(input('''O que você quer fazer agora? 
============================
    1. Ver suas tarefas
    2. Adicionar tarefa
    3. Editar status de tarefa
    4. Sair
    -> '''))

    if escolha == 1:
        ver_tarefa()

    if escolha == 2:
        add_tarefa()

    if escolha == 3:
        edit_tarefa()

    if escolha == 4:
        break