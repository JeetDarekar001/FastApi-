from typing import Union
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

BOOKS={
    'book_1':{'title':'Title ONE','author':'Author ONE'},
    'book_2':{'title':'Title TWO','author':'Author TWO'},
    'book_3':{'title':'Title THREE','author':'Author THREE'},
    'book_4':{'title':'Title FOUR','author':'Author FOUR'},
}
class DirectionName(str,Enum):
    north="North"
    south="South"
    east="East"
    west="West"

@app.get("/")
def read_root():
    return BOOKS


@app.get("books/mybook")
async def read_favorite_book():
    return {"book_title":"My Favoriate book"}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id":book_id}


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