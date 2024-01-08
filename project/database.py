from project.models import Books, Session
from icecream import ic

def query_list_all_books() -> list:  #   LIST OF ALL BOOKS (DICTS) IN THE DATABASE
    currentSession = Session()
    
    try:
        book_data = currentSession.query(Books).all()
        
        if book_data:
            books = ic([i.__dict__ for i in book_data])
            
            for i in books:
                del i['_sa_instance_state']
                
            currentSession.close()
            return ic(books)
        
        else:
            raise FileNotFoundError #   EM CASO DE BANCO DE DADOS VAZIO 404
        
    except Exception as e:
        currentSession.rollback()
        currentSession.close()
        raise e

def query_book_by_title(title:str) -> dict or Exception or ValueError:
    currentSession = Session()
    try:
        book_data = currentSession.query(Books).filter_by(title=title).first()
        
        if book_data:
            currentSession.close()  
            ans = ic(book_data.__dict__)
            del ans['_sa_instance_state']
            return ic(ans)
        
        else:
            currentSession.close()
            raise ValueError(f"There is no book with title = {title} in database")
        
    except Exception as e:
        currentSession.close()
        raise e

def insert_book_in_database(title:str, author:str, description: str, file_path:str):
    currentSession = Session()
    try:
        unique_validation = query_book_by_title(title=title)
        raise NameError(f"There is already a book with title {title} registered in database.")
    except ValueError:
        pass
    except NameError as e:
        raise e
    
    try:
        book = Books(
            title=title,
            author=author,
            description=description,
            file_path=file_path
        )
        
        currentSession.add(book)
        currentSession.commit()
        currentSession.close()
        return {"message": "Book registered succesfuly.", "status_code": 200}

    except Exception as e:
        currentSession.rollback()
        currentSession.close()
        raise e