import sqlite3

# CRIAÇÃO DO BANCO DE DADOS
# Execute este script para criação do banco de dados
def create_database():
    with sqlite3.connect('banco.db') as conn:
        cur = conn.cursor()
        with open('books.sql', 'r') as script:
            cur.executescript(script.read())

if __name__ == "__main__":
    create_database()