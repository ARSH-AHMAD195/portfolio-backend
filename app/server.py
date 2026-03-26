from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import setting
from routes import project_route
from core.database import Base, engine
import os


def create_app():
    project_name, project_version = setting.get_project_config()
    
    app = FastAPI(
        title=project_name,
        version=project_version
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Only create tables in development
    if os.getenv("ENV") == "development":
        Base.metadata.create_all(bind=engine)

    app.include_router(
        project_route.router
    )

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )