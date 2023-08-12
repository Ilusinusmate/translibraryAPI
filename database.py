import mysql.connector
import json

# CONFIGURE ESTE DICIONÁRIO SEGUNDO A CONFIGURAÇÃO DO SEU BANCO DE DADOS

config = {
    'user': 'root',
    'password': '12345678', # Certifique-se de por a senha correta
    'host': 'localhost',
    'port': '3306', # A porta pode variar de acordo com sua configuração
    'database': 'library',
    'raise_on_warnings': True
}

def searchBookByID(id: int, config: dict = config): # id: int, config: json/dict -> querry: json
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = f"SELECT * FROM books WHERE id = {id}"
    cursor.execute(query)
    book_data = cursor.fetchone()

    cnx.close()

    if book_data:
        book = {
            'id': book_data[0],
            'title': book_data[1],
            'author': book_data[2],
            'description': book_data[3],
            'first_chapter': book_data[4]
        }
        return json.dumps(book, indent=4)
    else:
        return json.dumps({'error': 'Book not found'}, indent=4)

def searchBookByTitle(title:str, config: dict = config): # title: str, config: json/dict -> querry: json
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = f"SELECT * FROM books WHERE title = {title}"
    cursor.execute(query)
    book_data = cursor.fetchone()

    cnx.close()

    if book_data:   
        book = {
            'id': book_data[0],
            'title': book_data[1],
            'author': book_data[2],
            'description': book_data[3],
            'first_chapter': book_data[4]
        }
        return json.dumps(book, indent=4)
    else:
        return json.dumps({'error': 'Book not found'}, indent=4)

#NOT IMPLEMENTED (For front-end choice hub)
def titles():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = f"SELECT name from books;"
    cursor.execute(query)
    book_data = cursor.fetchone()

    cnx.close()

    if book_data:   
        book = {
            'id': book_data[0],
            'title': book_data[1],
            'author': book_data[2],
            'description': book_data[3],
            'first_chapter': book_data[4]
        }
        return json.dumps(book, indent=4)
    else:
        return json.dumps({'error': 'Book not found'}, indent=4)

if __name__ == "__main__":
  #PARA TESTES
  book_json = searchBookByID(1)
  print(book_json)
