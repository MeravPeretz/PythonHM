from datetime import datetime
from enum import Enum

import uvicorn
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator


router = APIRouter()

class StatusEnum(str, Enum):
    open = 'open'
    close = 'close'

class User(BaseModel):
    id: str
    firstName: constr(pattern=r"^[a-zA-Z0-9_]+$")
    lastName: constr(pattern=r"^[a-zA-Z0-9_]+$")
    birthdate: datetime

    @field_validator('birthdate')
    def check_Des(cls, bd:datetime):
        if bd.year>datetime.now().year:
            raise ValueError('not correct date')
        return bd

    @field_validator('id')
    def check_Des(cls, id):
        if len(id) !=9:
            raise ValueError('not correct id')
        return id

Users={}


@router.get("/")
async def task():
    return Users
    raise HTTPException(status_code=404, detail="oops... an error occurd")


@router.post("/")
async def add_user(user: User):
    try:
        Users[user.id]=user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@router.put("/{id}", response_model=User)
async def update_user(id: str, item: User):
    update_item_encoded = jsonable_encoder(item)
    Users[id] = update_item_encoded
    return update_item_encoded



@router.delete("/{id}")
async def delete_user(id: str):
    del Users[id]
    return {"message": "Item deleted"}

