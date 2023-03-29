from typing import Union
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
    
@app.get("/clientes")
async def get_all_clients():
    
    return [{"quantidade_clientes":2}, {"clientes":[{"nome": "diego", "idade": 18}, {"nome":"angelo", "idade":17}]}]