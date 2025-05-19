from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
  email : EmailStr
  password : str
  
  friends : list = []
  invites : list = []