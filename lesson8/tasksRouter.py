from enum import Enum

import uvicorn
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator


router = APIRouter()

class StatusEnum(str, Enum):
    open = 'open'
    close = 'close'

class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    Des: str
    id: int
    status: StatusEnum

    @field_validator('Des')
    def check_Des(cls, Des):
        if len(Des) > 100:
            raise ValueError('error')
        return Des

    @field_validator('id')
    def check_Des(cls, id):
        if id > 100:
            raise ValueError('error')
        return id

Tasks={}


@router.get("/")
async def task():
    return Tasks
    raise HTTPException(status_code=404, detail="oops... your task didn't find")


@router.post("/")
async def add_task(task: Task):
    try:
        Tasks[task.id]=task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@router.put("/{id}", response_model=Task)
async def update_task(id: int, item: Task):
    update_item_encoded = jsonable_encoder(item)
    Tasks[id] = update_item_encoded
    return update_item_encoded



@router.delete("/{id}")
async def delete_task(id: int):
    del Tasks[id]
    return {"message": "Item deleted"}


