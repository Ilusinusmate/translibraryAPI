from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONFIG
Engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker(bind=Engine)

class Books(Base):
    __tablename__ = "books"  # Correção aqui

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    about = Column(String(255), nullable=False)
    book = Column(BLOB, nullable=False)

    def __repr__(self):
        return f"""
            'id': {self.id},
            'title': {self.title},
            'author': {self.author},
            'about': {self.about},
            'book': {str(self.book)}
        """
    
    def __str__(self):
        return self.__repr__()

# CREATE ALL TABLES (JUST RUN IF THERE'S NO DATABASE ALREADY CREATED)
if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)  # Correção aqui
