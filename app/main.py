import os
import importlib
from fastapi import FastAPI
from pathlib import Path

app = FastAPI()

# root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

def register_routes(base_dir: str, base_module: str = "app.routes"):
    """
    Recursively register routes from directory structure
    """
    routes_path = Path(base_dir)
    
    for root, dirs, files in os.walk(routes_path):
        if "index.py" in files:
            # Convert path to module notation
            rel_path = Path(root).relative_to(routes_path)
            module_path_parts = rel_path.parts
            
            if module_path_parts:
                # Format: app.routes.module.submodule
                module_path = f"{base_module}.{'.'.join(module_path_parts)}.index"
            else:
                module_path = f"{base_module}.index"
            
            try:
                # Import route module
                module = importlib.import_module(module_path)
                
                if hasattr(module, "router"):
                    # Generate prefix from path
                    route_prefix = "/" + "/".join(module_path_parts)
                    
                    app.include_router(
                        module.router,
                        prefix=route_prefix,
                        tags=[module_path_parts[-1].capitalize()] if module_path_parts else ["Root"]
                    )
                else :
                    print(f"[ERROR] No router found in {module_path}")
                    
            except ImportError as e:
                print(f"Error importing {module_path}: {e}")

# Initialize route registration
ROUTES_DIR = os.path.join(os.path.dirname(__file__), "routes")
register_routes(ROUTES_DIR)

#  pip freeze > requirements.txt