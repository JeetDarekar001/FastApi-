from typing import Optional
from pydantic import BaseModel,Field
from uuid import UUID

class Book(BaseModel):
    id:UUID
    title :str=Field(min_length=1)
    author:str=Field(min_length=1,max_length=100)
    description:Optional[str]=Field(title='Description of book',max_length=100,min_length=1)
    rating:int=Field(gt=-1,lt=101)
#Data valiaiton