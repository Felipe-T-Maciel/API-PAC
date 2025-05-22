from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class UserPostDTO(BaseModel):
  email : EmailStr
  password : str
  
  friends: Optional[List] = Field(default_factory=list)
  invites: Optional[List] = Field(default_factory=list)