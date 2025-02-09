from fastapi import FastAPI
from typing import Union

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World Piyush"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



#  pip freeze > requirements.txt