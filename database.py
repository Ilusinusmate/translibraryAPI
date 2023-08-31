from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from typing import Union, Optional, Tuple

#config
Engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker(bind=Engine)

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    about = Column(String(255), nullable=False)
    book = Column(BLOB, nullable=False)

    def __repr__(self):
        return f"""
            'id': {self.id},\n
            'title': {self.title},\n
            'author': {self.author},\n
            'about': {self.about},\n
            'book': {str(self.book)}
        """ 
    def __str__(self):
        return self.__repr__(self)

def allBooks():
    currentSession = Session()
    try:
        book_data = currentSession.query(Books).all()
        return book_data
    except Exception as e:
        raise Exception(e)

def searchBookByID(id:int): # id: int -> json (title, author, about), file (pdf : bytes)
    currentSession = Session()
    book_data = currentSession.query(Books).filter_by(id=id).first()

    if book_data:   
        book = {
            'id': book_data.id,
            'title': book_data.title,
            'author': book_data.author,
            'about': book_data.about
        }
        return (json.dumps(book, indent=4), book_data.book)
    else:
        return 404

def searchBookByTitle(title:str): # title: str -> json (title, author, about), file (pdf : bytes)
    currentSession = Session()
    book_data = currentSession.query(Books).filter_by(title=title).first()

    if book_data:   
        book = {
            'id': book_data.id,
            'title': book_data.title,
            'author': book_data.author,
            'about': book_data.about
        }
        return (json.dumps(book, indent=4), book_data.book)
    else:
        return 404

#NOT IMPLEMENTED (For front-end choice hub)
def titles():
    currentSession = Session()
    data = [i.title for i in currentSession.query(Books).all()]
    if data:
        return data
    else:
        return 404

async def addBook(title, author, about: Optional[str], book: Union[str, bytes]):

    currentSession = Session()

    if isinstance(book, str):
        book = bytes(book, encoding="utf-8")

    data_insert = Books(title=title, author=author, about=about, book=book)
    try:
        currentSession.add(data_insert)
        currentSession.commit()
        return 201
    except Exception as e:
        currentSession.rollback()
        raise Exception(e, "RollBack executed.")

def delBookById(id:int):
    currentSession = Session()
    try:
        currentSession.query(Books).filter_by(id=id).delete()
    except Exception as e:
        currentSession.rollback()
        raise Exception(e, "RollBack executed")

def delBookByIdRange(start: int, end: int):
    for _ in range(start, end+1):
        delBookById(start)

def delBookByTitle(title:str):
    currentSession = Session()
    try:
        currentSession.query(Books).filter_by(title=title).delete()
    except Exception as e:
        currentSession.rollback()
        raise Exception(e, "RollBack executed")

if __name__ == "__main__":
  #PARA TESTES

  print(searchBookByID(1))
  print(searchBookByTitle("Harry Potter and the Sorcerers Stone"))
  
