from fastapi import UploadFile, Query, File, Body
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException
import os
from icecream import ic

from project import app, BOOKS_DIRECTORY
from project.database import query_list_all_books, insert_book_in_database, query_book_by_title
from project.validations import ValidationBook, is_valid_book_file
from project.translation import get_available_languages, translate_file, translate_text


#   REDIRECT SESSION


@app.get("/documentation")
@app.get("/home")
@app.get("/")
def redirect_docs():
    return RedirectResponse(url="http://localhost:8000/docs", status_code=301)


#   CRUD BOOKS SECTION


@app.get("/books")
def list_books():
    try:
        query = query_list_all_books()
        return JSONResponse(content=query, status_code=200)
    
    except FileNotFoundError:
        return HTTPException(status_code=404, detail="There is no books in the database.")
    
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.get("/books/query")
def get_book_by_title(
    title: str = Query(description="Title of the book")
) -> FileResponse:
    
    try:
        query = query_book_by_title(title=title)
        ic(query)
        return FileResponse(query["file_path"], status_code=200)
        
    except ValueError as e:
        return HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/books/insert")
def insert_book(
    title: str = Query(description="Title of the book"),
    author: str = Query(description="Author of the book, on it's own language"),
    description: str = Query(description="Short description about the book"),
    file : UploadFile = File(description="The book in pdf format")
) -> JSONResponse or HTTPException:
    
    #    PARAMETERS VALIDATION
    try:
        _ = ValidationBook(title=title, author=author, description=description).dict(exclude_unset=True)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    
    #    FILE VALIDATION
    if not is_valid_book_file(file.filename):
        return HTTPException(status_code=400, detail="File must be pdf or txt file.")
    
    content = file.file.read()
    file_path = BOOKS_DIRECTORY+"\\"+file.filename
    
    with open(file_path, "wb") as path:
        
        #   SAVE FILE INFORMATION ON DATABASE AND WRITE
        try:
            insert_book_in_database(
                title=title,
                author=author,
                description=description,
                file_path=file_path
            )
        
            path.write(content)
        
        except NameError as e:
            return HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            return HTTPException(status_code=500, detail=str(e))
        
    #   RETURN RESPONSE    
    return JSONResponse(content={
        "title":title,
        "author": author,
        "description": description,
        "file": file.filename,
        "message": "Your file has been saved sucessfuly."
        },
        status_code=200,
        )


#   TRANSLATION SECTION


@app.get("/books/translation/all")
def list_all_available_languages() -> dict:
    return get_available_languages()



@app.get("/books/translation")
def translate_book(
    book_name:str = Query(description="Book name"),
    target_language: str = Query(description="Destination Language, for more details '/books/translation/all'")
) -> FileResponse or HTTPException:
    
    try:
        output_path = translate_file(book_name, target_language)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
    if os.path.exists(output_path):
        return FileResponse(output_path, status_code=200)
   
    else:
        return HTTPException(status_code=500, detail=f"{output_path} does not exists.")

@app.post("/translation")
def translation(
    text: str = Body(description="Text to translate"),
    target_language: str = Query(description="Destination Language, for more details '/books/translation/all'")
):
    return JSONResponse(status_code=200, content={"translated_text": translate_text(text=text, target_lang=target_language)})