from project.models import Books, Session
from icecream import ic

def query_list_all_books():
    currentSession = Session()
    try:
        book_data = currentSession.query(Books).all()
        
        if book_data:  
             
            books = ic([i.__dict__ for i in book_data])
            currentSession.close()
            return books
        
        else:
            currentSession.close()
            return {"status_code":404,
                    "sucess": False,
                    "error": "Not found",
                    "detail": "There is no book in 'Books' table"}
        
    except Exception as e:
        return {"status_code":500,
                "sucess": False,
                "error": str(e)}
    
def insert_book_in_database():
    pass