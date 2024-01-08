from sqlalchemy import MetaData, Column, Integer, String, BLOB
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_NAME = "banco.db"

# CONFIG
Engine = create_engine(f"sqlite:///{DATABASE_NAME}")
meta_data = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=Engine)

class Books(Base):
    __tablename__ = "books"  

    title = Column(String(255), primary_key=True)
    author = Column(String(40), nullable=False)
    description = Column(String(255), nullable=False)
    file_path = Column(String(300), nullable=False, unique=True)

    def __repr__(self):
        return f"""
            'id': {self.id},
            'title': {self.title},
            'author': {self.author},
            'description': {self.description},
            'file_path': {str(self.file_path)}
        """
    
    def __str__(self):
        return self.__repr__()

# CREATE ALL TABLES (JUST RUN IF THERE'S NO DATABASE ALREADY CREATED)
if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)  # Correção aqui
