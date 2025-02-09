from fastapi import FastAPI
from typing import Union
from mangum import Mangum  # Required for Vercel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World Piyush"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Mangum adapter for Vercel compatibility
handler = Mangum(app)

#  pip freeze > requirements.txt