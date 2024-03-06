from enum import Enum

import static as static
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, ValidationError

app=FastAPI()

id=0
def NextId():
    id=id+1
    return id

class Status(str,Enum):
    open="open"
    close="close"
class Task(BaseModel):
        id:int
        name:constr(min_length=1,max_length=20,pattern='^[a-zA-Z]+$')
        description:constr(max_length=200)
        status:Status
       # def __init__(self,_name:str,_description:str,_status:Status):
            # try:
            #     self.status=_status
            #     self.name=_name
            #     self.description=_description
            #     self.id=NextId()
            # except:
            #     raise ValueError()



tasks=[Task(id=0,name="java",description="lesson17",status=Status.open).dict()]

@app.get("/task")
async def returnAllTasks():
    return tasks

@app.post("/task")
async def addTask(task:Task):
    try:
        task.id=NextId()
        tasks.append(task.dict())
        return{"secced!":tasks}
    except :
        raise HTTPException(status_code=400, detail="oops... an error occurred")

@app.delete("/task/{id}")
async def deleteTask(id):
    taskTodelete=0
    for t in tasks:
        if t.get(id)==int(id) :
            taskTodelete=t
    if taskTodelete==0:
        raise HTTPException(status_code=404, detail="notFound")
    tasks.remove(t)
    return {"secced!":tasks}

if __name__ == '__main__':
    uvicorn.run("main:app" ,host="127.0.0.1", port=8080,reload=True)

