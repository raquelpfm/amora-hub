from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base

class Morador(Base):
    __tablename__ = "moradores"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)