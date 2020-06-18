from typing import TypedDict
from datetime import datetime

class NoteInterface(TypedDict , total = False):
    id:int
    title:str 
    note: str
    created_date: datetime
    updated_date:datetime
    author_id: int 