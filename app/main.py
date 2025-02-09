import os
import importlib
from fastapi import FastAPI
from typing import Union

app = FastAPI()

# Define a GET endpoint for the root URL
@app.get("/")
def read_root():
    # Return a simple greeting message
    return {"Hello": "World Piyush"}

# Directory containing route modules
ROUTES_DIR = os.path.join(os.path.dirname(__file__), "routes")

# Iterate over each folder in the routes directory
for folder in os.listdir(ROUTES_DIR):
    folder_path = os.path.join(ROUTES_DIR, folder)

    # Check if the folder contains an index.py and is a directory
    if os.path.isdir(folder_path) and f"index.py" in os.listdir(folder_path):
        module_path = f"routes.{folder}.index"
        module = importlib.import_module(module_path)
        
        # Check if the module has a router attribute and include it in the app
        if hasattr(module, f"router"):
            router = getattr(module, f"router")
            app.include_router(
                router,
                prefix=f"/{folder}",
                tags=[folder.capitalize()]
            )

#  pip freeze > requirements.txt