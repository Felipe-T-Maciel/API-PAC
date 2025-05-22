from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
  email : EmailStr
  image: str = None
  friends : list = []
  invites : list = []