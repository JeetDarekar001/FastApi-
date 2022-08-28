
from email import header
from typing import Optional
from uuid import UUID
from fastapi import FastAPI,HTTPException,Request,status
from fastapi import Form, Header

from starlette.responses import JSONResponse
from models import Book,BookNoRating


app = FastAPI()

#Initilized the BOOKS=[] for adding books when read_all_boosk() is caled.
BOOKS=[]

class NegtiveNumberException(Exception):
    """
    NegtiveNumberException is custom class for raising custom exception
    """
    def __init__(self, books_to_return):
        self.books_to_return=books_to_return

#Custom exception handler derived from NegtiveNumberException class
@app.exception_handler(NegtiveNumberException)
async def neg_number_exception_handler(request:Request, exception:NegtiveNumberException):
    return JSONResponse(status_code=418,  
                content={"message":"Number of books cannot be negiteve"}
    )
# New Status code incase of negtieve number as input.
# Custom error message for user

@app.get("/")
async def read_all_books(books_to_return:Optional[int]=None):
    """
    If no book data is found, create_book_no_api() is invoked to initilized BOOKS list, 
    to help
    """
    if len(BOOKS)<1:
        create_book_no_api()

    # Incase of negtieve number as input then custom exception is raised. 
    if books_to_return and books_to_return <0:
        raise NegtiveNumberException(books_to_return=books_to_return)

    if books_to_return and len(BOOKS)>=books_to_return>0:
        i=1
        newbooks=[]
        while i<=books_to_return:
            newbooks.append(BOOKS[i-1])
        return newbooks

    return BOOKS

# Searching book by UUID
# Initially UUID is fetched by running Get all books function, later UUID is fetched by calling /book/UUID  
@app.get("/book/{book_id}")
async def read_book(book_id:Optional[UUID]):
    for x in BOOKS:
        if x.id==book_id:
            return x

# When this api is called, it will not return rating to user.
# THis method is used to restrict some fields in case of response api.
# In this case we are restricitng the rating field in the response model.
@app.get("/book/rating/{book_id}",response_model=BookNoRating)
async def read_book_no_rating(book_id:Optional[UUID]):
    for x in BOOKS:
        if x.id==book_id:
            return x
    raise raise_item_cannot_be_foud_exception()


# Adding status code of 201 signifyis something is created
@app.post('/',status_code=status.HTTP_201_CREATED)
async def create_book(book:Book):
    BOOKS.append(book)
    return book

# Header class is used to create a custom header.
@app.post('/header')
async def read_header(random_head:Optional[str]=Header(None)):
    return {"Random-Header":random_head}

# How to use form data username and password
@app.post("/book/login")
async def book_login(username:str=Form(),password:str=Form()):
    return {'username':username,"password":password}

# How to use form data username and password
@app.post("/book/login/header/")
async def book_login_username_and_password_in_header(book_id: int,username:Optional[str]=Header(None),password:Optional[str]=Header(None)):
    if username and password and username=="FastAPIUser" and password=="test1234":
        #return {'username in header':username,"password in header":password}
        return BOOKS[book_id-1]   
    else:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )


#Put Request
@app.put("/{book_id}")
async def update_book(book_id:UUID, book:Book):
    counter=0
    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            BOOKS[counter-1]=book
            return BOOKS[counter-1]
    raise_item_cannot_be_foud_exception()


#Delete Request by book_id
@app.delete('/{book_id}')
async def delete_book(book_id:UUID):
    counter=0
    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            del BOOKS[counter-1]
            return f'book {book_id} deleted'
    raise_item_cannot_be_foud_exception()


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

#Exception Block for 404 book not found for updating and deleting
def raise_item_cannot_be_foud_exception():
    raise HTTPException(status_code=404,
                    detail="Book Not Found",
                    headers={"X_header-Error":"Nothing to found for UUID"})


