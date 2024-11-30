import sqlite3 as sq
import os

def conecta_db():
    db_path = os.path.join(os.path.dirname(__file__), 'tarefas.db')
    return sq.connect(db_path)


def cria_tabela():
    with conecta_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                nome TEXT PRIMARY KEY,
                status BOOLEAN
            )     
    ''')


def salva_no_db(tarefa, status):
    with conecta_db() as conn:
        conn.execute('''
            INSERT OR REPLACE INTO tarefas (nome, status)
            VALUES (?, ?)
        ''', (tarefa, status))


def retorna_do_db():
    with conecta_db() as conn:
        cursor = conn.execute('SELECT * FROM tarefas')
        dados = cursor.fetchall()
        lista_tarefas = [(nome, bool(status)) for nome, status in dados]

        return lista_tarefas


def exclui_tarefa(nome):
    with conecta_db() as conn:
        conn.execute('DELETE FROM tarefas WHERE nome = ?', (nome,))