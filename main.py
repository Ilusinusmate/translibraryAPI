from fastapi import FastAPI, Query
from database import searchBookByID
from googletranslate import async_translate
import uvicorn
import json
import asyncio

app = FastAPI()

@app.get("/")
def home():
    # Rota default
    return "Welcome to the Book API"

@app.get("/books")
async def querry(
    id: int = Query(..., description="ID used to access the book - PRIMARY KEY"),
    lang: str = Query(..., description="Language to translate the book")
):
    # """
    # Rota para obter informações de um livro com tradução para o idioma especificado.
    # Args:
    #     id (int): O ID do livro a ser acessado.
    #     lang (str): O idioma alvo para a tradução.

    # Returns:
    #     dict: As informações do livro traduzidas.
    # """

    book = searchBookByID(id)
    book = json.loads(book)  
    tasks = [
        async_translate(book["title"], lang, "auto"),
        async_translate(book["description"], lang, "auto"),
        async_translate(book["first_chapter"], lang, "auto")
    ]

    translated_title, translated_description, translated_first_chapter = await asyncio.gather(*tasks)

    translated_book = {
        "title": translated_title,
        "author": book["author"],
        "description": translated_description,
        "first_chapter": translated_first_chapter
    }
    return translated_book

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
