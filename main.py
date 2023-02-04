import os
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, List
from fastapi.params import Body
import time
from sqlalchemy.orm import Session
import models, schemas, utils
from database import engine, get_db 
from routers import post, user, auth  
database_password = os.environ.get("DATABASE_PASSWORD")

if not database_password:
    raise Exception("The environment variable DATABASE_PASSWORD must be set.")

models.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'FastAPI', user = 'postgres', 
                                password = {database_password}, cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connection to database failed")
        print("error: ", error)
        time.sleep(2)
 
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)