from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1 import routes_users
from app.middlewares.trademark_headers import TrademarkMiddleware

def create_app():
    app = FastAPI(
        title="FastAPI",
        description="FastAPI API Documentation, with Swagger UI",
        version="0.0.1",
        
        redirect_slashes=True,
        openapi_url="/openapi-contract.json",
        openapi_tags=[
            {'name': '👤 Users', 'description': 'User related endpoints.'}
        ],
        lifespan=lifespan
    )
    
    # Middlewares
    app.add_middleware(TrademarkMiddleware)
    
    # Routes
    app.include_router(routes_users.router, prefix="/api/v1/users", tags=["👤 Users"])
    
    return app

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield