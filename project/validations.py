from pydantic import BaseModel, constr
from fastapi import UploadFile
from typing import Optional
import imghdr

from project import ALLOWED_BOOK_TYPES

from icecream import ic

class ValidationBook(BaseModel):
    title: constr(max_length=255)
    author: constr(max_length=40)
    description: constr(max_length=255)
    
def is_valid_book_file(file_name: str) -> bool:
    #   VULNERABILIDADE
    return any(file_name.endswith(i) for i in ALLOWED_BOOK_TYPES)