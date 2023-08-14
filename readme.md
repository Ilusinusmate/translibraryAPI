# TransLibrary

## API de Disponibilização e Tradução de livros.

A aplicação desenvolvida roda em instância local e no momento não está em estágio de produção.

## Como testar a aplicação:

• Crie o banco de dados SQLite executando o script "sqlite.py" caso o mesmo não exista.

• Ative o Virtual Environment "venv"

• Rode o arquivo main.py

• Faça requisições HTTP para "https://localhost:8000/books"

• Para acessar a documentação da API, acesse "https://localhost:8000/docs" em um navegador


< TODAS AS DEPENDÊNCIAS NA VENV >


- main.py

Utilização do framework FastAPI para integração ao banco de dados MySQL, documentação da API e definição de rotas URL para requisições HTTP.

- database.py
  
Integração com o banco de dados MySQL hospedado em instância local.

- googletranslate.py

Integração com API do google. Utilizada para a tradução dos livros.

- books.sql 

Para a utilização de um banco de dados no formato utilizado,
rode o arquivo sql e terá um banco de dados para teste.

- sqlite.py

Script para formação do banco de dados de teste a partir de
"books.sql", execute somente uma vez.

- banco.sqlite

Banco de dados no formato de arquivo, gerenciado pela lib
sqlite3 built-in do Python3.
