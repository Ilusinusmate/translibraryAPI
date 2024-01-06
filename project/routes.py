from fastapi import UploadFile, Query, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import HTTPException

from project import app, BOOKS_DIRECTORY
from project.database import query_list_all_books
from project.validations import ValidationBook, is_valid_book_file



@app.get("/books")
def list_books():
    query = query_list_all_books()
    return JSONResponse(content=query, status_code=query["status_code"])



@app.post("/books/insert")
def insert_book(
    title: str = Query(description="Title of the book"),
    author: str = Query(description="Author of the book, on it's own language"),
    description: str = Query(description="Short description about the book"),
    file : UploadFile = File(description="The book in pdf format")
):
    
    #    PARAMETERS VALIDATION
    try:
        _ = ValidationBook(title=title, author=author, description=description).dict(exclude_unset=True)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    
    
    #    FILE VALIDATION
    if not is_valid_book_file(file.filename):
        return HTTPException(status_code=400, detail="File must be pdf or txt file.")
    
    content = file.file.read()
    
    with open(BOOKS_DIRECTORY+"\\"+file.filename, "wb") as path:
        path.write(content)
        
    return [title, author, description, file]