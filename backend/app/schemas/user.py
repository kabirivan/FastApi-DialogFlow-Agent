from app.models.user import UserBase
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID
from enum import Enum

class IUserCreate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    password : Optional[str]
    hashed_password : Optional[str]
    email: EmailStr
    is_superuser: bool = False
    role_id: Optional[UUID]
        
class IUserReadWithoutGroups(UserBase):
    id: UUID

class IUserRead(UserBase):
    id: UUID    

class IUserUpdate(BaseModel):
    id : int
    email : EmailStr
    is_active : bool = True

class IUserStatus(str, Enum):
    active = 'active'
    inactive = 'inactive'