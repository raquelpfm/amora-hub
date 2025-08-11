from pydantic import BaseModel, EmailStr

# Propriedades base compartilhadas
class MoradorBase(BaseModel):
    email: EmailStr
    nome_completo: str

# Schema para a criação de um morador (recebido pela API)
class MoradorCreate(MoradorBase):
    password: str

# Schema para a leitura de um morador (enviado pela API)
class MoradorRead(MoradorBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True