from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Cria o "motor" de conexão assíncrono com o banco
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Cria uma fábrica de sessões assíncronas
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    class_=AsyncSession
)