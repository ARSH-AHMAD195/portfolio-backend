from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.projects import Project
from app.schema.projects import ProjectCreate

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    data = project.model_dump()

    # 👇 convert URL fields to string
    for key in ["image_url", "github", "live_url"]:
        if data.get(key):
            data[key] = str(data[key])

    new_project = Project(**data)

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()