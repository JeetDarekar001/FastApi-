
from fastapi import FastAPI
from models import Book
app = FastAPI()

BOOKS=[]

@app.get("/")
async def read_all_books():
    return BOOKS

@app.post('/')
async def create_book(book:Book):
    BOOKS.append(book)
    return book