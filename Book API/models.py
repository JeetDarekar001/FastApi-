from typing import Optional
from pydantic import BaseModel,Field
from uuid import UUID

class Book(BaseModel):
    id:UUID
    title :str=Field(min_length=1)
    author:str=Field(min_length=1,max_length=100)
    description:Optional[str]=Field(title='Description of book',max_length=100,min_length=1)
    rating:int=Field(gt=-1,lt=101)  
    #Data validation : Added Field
    #Changing the default configuration
    class Config:
        schema_extra={
            "example":{
                "id":"913302d8-0e41-43b8-86f4-a6e044714398",
                "title":"Computer Science Pro",
                "author":"Abhijit",
                "description":"A Very Nice book",
                "rating":30
            }
        }