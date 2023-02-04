from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
import models, schemas
from typing import List
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix = "/posts",
    tags = ['POSTS']
)

@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):
    
    #cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post).all()
    return posts
    
@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post: schemas.PostCreate, db : Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *""", 
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

@router.get("/{id}", response_model=schemas.Post)
async def get_post(id:int, db : Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first() 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"post with id: {id} was not found")
    print(post)
    return post

@router.delete("/delete/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db : Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id) 

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"post with id: {id} was not found") 
        
    post.delete(synchronize_session=False)
    db.commit()
        

@router.put("/{id}", response_model=schemas.Post)
async def update(id:int, updated_post:schemas.PostCreate, db : Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()