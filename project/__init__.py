#   THIRDPARTY IMPORTS
from fastapi import FastAPI
import os

#   SETUP
app = FastAPI()
BOOKS_DIRECTORY = __file__.removesuffix("\\__init__.py") + "\\books"
if not os.path.exists(BOOKS_DIRECTORY):
    os.makedirs(BOOKS_DIRECTORY)
ALLOWED_BOOK_TYPES = {"pdf", "txt"}


#   INICIALIZATE FILES

from project import routes
from project import models
from project import database
from project import validations