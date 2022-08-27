from typing import Union

from fastapi import FastAPI

app = FastAPI()

BOOKS={
    'book_1':{'title':'Title ONE','author':'Author ONE'},
    'book_2':{'title':'Title TWO','author':'Author TWO'},
    'book_3':{'title':'Title THREE','author':'Author THREE'},
    'book_4':{'title':'Title FOUR','author':'Author FOUR'},
}

@app.get("/")
def read_root():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id":book_id}