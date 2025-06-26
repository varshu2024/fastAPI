from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate, 
    user_id: int, 
    db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items