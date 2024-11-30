from db import salva_no_db, retorna_do_db, exclui_tarefa

def ver_tarefa():
    lista_tarefas = retorna_do_db()
    if len(lista_tarefas) == 0:
        print('=' * 32)
        print('Nenhuma tarefa adicionada ainda.')
        print('=' * 32)
    else:
        print('=' * 20)
        
        for nome, status in lista_tarefas:
            status_texto = 'Concluída' if status else 'Pendente'
            print(f'{nome} - {status_texto}')
            print('*' * 20)
        print('=' * 20)


def add_tarefa():
    tarefa = str(input('Qual a tarefa? '))
    status = False
    print('=' * 28)
    salva_no_db(tarefa, status)


def edit_tarefa():
    lista_tarefas = retorna_do_db()
    print('=' * 20)
    print('Qual tarefa voce quer editar? ')

    for i, nome in enumerate(tarefa[0] for tarefa in lista_tarefas):
        print(f'{i}: {nome}')

    escolha = int(input('->'))
    print('=' * 20)

    if 0 <= escolha <len(lista_tarefas):
        tarefa = lista_tarefas[escolha]
        nome, status = tarefa

        acao = int(input(('''
    1. Marcar como concluída
    2. Excluir
    -> ''')))


        if acao == 1:
            if status == True:
                print('A tarefa já está concluída.')
                print('=' * 20)
            else:
                status = True
                salva_no_db(nome, status)
                print('=' * 20)
                print('Alterado com sucesso')
        if acao == 2:
            exclui_tarefa(nome)
            print(f'A tarefa "{nome}" foi removida com sucesso.')
            if len(lista_tarefas) == 0:
                print('A lista agora está vazia.')
                print('=' * 20)
            else:
                ver_tarefa()
    else:
        print('Escolha inválida. Tente novamente.')