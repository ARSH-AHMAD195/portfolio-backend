from pydantic import BaseModel, HttpUrl

class ProjectCreate(BaseModel):
    title: str
    description: str
    tech_stack: str
    github: str
    live_url: str
    image_url: HttpUrl 
    featured: bool = False


class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True