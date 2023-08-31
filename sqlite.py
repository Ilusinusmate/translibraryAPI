import sqlite3

# CRIAÇÃO DO BANCO DE DADOS
# Execute este script para criação do banco de dados

with sqlite3.connect('banco.db') as conn:
    cur = conn.cursor()
    with open('books.sql', 'r') as script:
        cur.executescript(script.read())

