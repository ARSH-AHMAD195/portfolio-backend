from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    tech_stack = Column(String)
    github = Column(String)
    live_url = Column(String)
    image_url = Column(String)
    featured = Column(Boolean, default=False)