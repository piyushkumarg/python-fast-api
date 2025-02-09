import os
import importlib
from fastapi import FastAPI

app = FastAPI()

# root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

ROUTES_DIR = os.path.join(os.path.dirname(__file__), "routes")
for folder in os.listdir(ROUTES_DIR):
    folder_path = os.path.join(ROUTES_DIR, folder)
        
    if os.path.isdir(folder_path) and "index.py" in os.listdir(folder_path):
        # Use absolute imports for serverless environments
        module_path = f"app.routes.{folder}.index"
        module = importlib.import_module(module_path)
            
        if hasattr(module, "router"):
            app.include_router(
                module.router,
                prefix=f"/{folder}",
                tags=[folder.capitalize()]
            )


#  pip freeze > requirements.txt