from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
  name : str
  username : str
  email : EmailStr
  password : str
  
  friends : list = []
  invites : list = []