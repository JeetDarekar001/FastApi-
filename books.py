from hashlib import new
from typing import Optional, Union
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

BOOKS={
    'book_1':{'title':'Title ONE','author':'Author ONE'},
    'book_2':{'title':'Title TWO','author':'Author TWO'},
    'book_3':{'title':'Title THREE','author':'Author THREE'},
    'book_4':{'title':'Title FOUR','author':'Author FOUR'},
}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id":book_id}

"""   
@app.get("books/mybook")
async def read_favorite_book():
    return {"book_title":"My Favoriate book"}

#Enum in FastAPI

class DirectionName(str,Enum):
    north="North"
    south="South"
    east="East"
    west="West"

@app.get("/direction/{direction_name}")
async def get_direction(direction_name : DirectionName):
    if direction_name == DirectionName.north:
        return {"direction":direction_name.north , "sub":"up"}
    if direction_name == DirectionName.south:
        return {"direction":direction_name.south , "sub":"down"}
    if direction_name == DirectionName.east:
        return {"direction":direction_name.east , "sub":"right"}
    if direction_name == DirectionName.west:
        return {"direction":direction_name.west , "sub":"left"}
"""
#Query Parameters
@app.get("/")
def read_books(skip_book:Optional[str]=None): #optional makes skip_book paramerts options;
    if skip_book:
        new_books=BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/{book_name}")
async def read_book(book_name:str):
    return BOOKS[book_name]


"""
@app.get("/")
async def read_all_books():
    return BOOKS
    """

#Post request
@app.post("/")
async def create_book(book_title,book_author):
    current_book_id=0

    if len(BOOKS)>0:
        for book in BOOKS:
            x=int(book.split('_')[-1])
            if x>current_book_id:
                current_book_id=x
    BOOKS[f'book_{current_book_id+1}']={'title':book_title,'author':book_author}
    return BOOKS[f'book_{current_book_id+1}']

#Put Request Updating book title and book author
@app.put("/{book_name}")
async def update_book(book_name:str,book_title:str,book_author:str):
    book_info={'title':book_title,'author':book_title}
    BOOKS[book_name]=book_info
    return book_info

@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book {book_name} Deleted'

#Read api with query paramerts
@app.get("/assignment/get/")
async def read_book_func(book_name):
    return BOOKS[book_name]    
