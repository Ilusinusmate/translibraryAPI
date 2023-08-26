from fastapi import FastAPI, Query, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response, JSONResponse
from database import searchBookByID, searchBookByTitle, addBook
from googletranslate import async_translate
from pdfs import bytesToPdf, delPdf
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

    delPdf("temp")

    if isinstance(id, int):
        book = searchBookByID(id)
    elif isinstance(id, str):
        book = searchBookByTitle(id)
    
    if book == 404:
        return HTTPException(404, "Book not found")

    pdfName = "temp"

    bytesToPdf(pdfBytes=book[1], pdfName=pdfName)
    book = json.loads(book[0])  

    tasks = [
        async_translate(book["title"], lang, "auto"),
        async_translate(book["description"], lang, "auto"),
    ]

    translated_title, translated_description,  = await asyncio.gather(*tasks)

    translated_book = {
        "title": translated_title,
        "author": book["author"],
        "description": translated_description,
    }
    
    return translated_book

@app.post("/books")
async def uploadBook(
    title: str = Query(description="Title of the book"),
    author: str = Query(description="Author of the book, on it's own language"),
    description: str = Query(description="Short description about the book"),
    file : UploadFile = File(description="The book in pdf format")
):
    await addBook(title, author, description, file.file.read())
    return JSONResponse(content={"message":"PDF Upload Successfuly"})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
