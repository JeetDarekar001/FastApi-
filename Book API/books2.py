
from optparse import Option
from typing import Optional
from uuid import UUID
from fastapi import FastAPI
from models import Book
app = FastAPI()

BOOKS=[]



@app.get("/")
async def read_all_books(books_to_return:Optional[int]=None):
    """
    If no book data is found, create_book_no_api() is invoked to initilized BOOKS list, 
    to help
    """

    if len(BOOKS)<1:
        create_book_no_api()
    
    if books_to_return and len(BOOKS)>=books_to_return>0:
        i=1
        newbooks=[]
        while i<=books_to_return:
            newbooks.append(BOOKS[i-1])
        return newbooks

    return BOOKS

#Searching book by UUID
@app.get("/book/{book_id}")
async def read_book(book_id:Optional[UUID]):
    for x in BOOKS:
        if x.id==book_id:
            return x

@app.post('/')
async def create_book(book:Book):
    BOOKS.append(book)
    return book

def create_book_no_api():
    """
    This blocks appends the book data whenever server restarts just to have data to perfom validation of RestApi's
    """
    
    book_1=Book(id="913302d8-0e41-43b8-86f4-a6e044714398",
    title="title1",
    author="author 1",
    description='Descripton 1',
    rating=90)
    book_2=Book(id="113302d8-0e41-43b8-86f4-a6e044714398",
    title="title2",
    author="author 2",
    description='Descripton 2',
    rating=80)
    book_3=Book(id="913304d8-0e41-43b8-86f4-a6e044714398",
    title="title 3",
    author="author 3",
    description='Descripton 3',
    rating=89)
    book_4=Book(id="913332d8-0e41-43b8-86f4-a6e044714398",
    title="title 4",
    author="author 4",
    description='Descripton 4',
    rating=10)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
