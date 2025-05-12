from app.models.User import User
from app.service.user_service import User_service
from fastapi import APIRouter
from app.models.DTO.user.UserPostDTO import UserPostDTO

userController = APIRouter()
user_service = User_service()

class User_Controller():
  @userController.post("/user/new_user")
  def create_user(user: UserPostDTO):
    existing_user = user_service.get_user_by_username(username=user.username)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    existing_user = user_service.get_user_by_email(email=user.email)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    new_user = user_service.create_user(user)
    return {"message": "Usuário Criado", "user": new_user}
  
  @userController.put("/user/update/{user_id}")
  def update_user(user: UserPostDTO, user_id: int):
    existing_user = user_service.get_user_by_username(username=user.username)
    if existing_user:
      if existing_user.id != user_id:
        return {"message":"Usuário já existe"}
    
    existing_user = user_service.get_user_by_email(email=user.email)
    if existing_user:
      if existing_user.id != user_id:
        return {"message":"Usuário já existe"}
    
    user = user_service.update_user(user_id, user)
    if not user:
      return {"message":"Usuário não encontrado"}
    return {"message": "Deu boa", "user": user}
  
  @userController.delete("/user/delete/{user_id}")
  def delete_user(user_id: int):
    if user_service.delete_user(user_id) != None:
      return {"message":"Usuário deletado"}
    return {"message":"Usuário não encontrado"}
  
  @userController.get("/user/{user_id}")
  def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
      return {"message":"Usuário não encontrado"}
    return {"message": "Deu boa", "user": user}