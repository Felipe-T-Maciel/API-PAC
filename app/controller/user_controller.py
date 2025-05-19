from app.models.User import User
from app.service.user_service import User_service
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth import create_access_token, verify_token
from app.models.DTO.user.UserPostDTO import UserPostDTO

userController = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_service = User_service()

class User_Controller():
  @userController.post("/register")
  def create_user(user: UserPostDTO):
    existing_user = user_service.get_user_by_email(email=user.email)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    existing_user = user_service.get_user_by_email(email=user.email)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    new_user = user_service.create_user(user)
    token = create_access_token(data={"sub": new_user.email})
    return {"access_token": token, "token_type": "bearer", "user": new_user}
  
  @userController.put("/user/update")
  def update_user(user: UserPostDTO, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
      return {"message":"Token inválido"}
    existing_user = user_service.get_user_by_email(email=user.username)
    if not existing_user:
      user = user_service.update_user(user.id, user)
      return {"user": user, "token": token}
  
  @userController.delete("/user/delete/{user_id}")
  def delete_user(user_id: int, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    if user_service.delete_user(user_id) != None:
      return {"message":"Usuário deletado"}
    return {"message":"Usuário não encontrado"}
  
  @userController.get("/user/{user_id}")
  def get_user_by_id(user_id: int):
    
    user = user_service.get_user_by_id(user_id)
    if not user:
      return {"message":"Usuário não encontrado"}
    return {"message": "Deu boa", "user": user}
  
  @userController.get("/login")
  def login(user: UserPostDTO):
    user = user_service.login(email=user.email, password=user.password)
    if user:
      token = create_access_token(data={"sub": user.email})
      return {"user": user, "token": token}
    if not user:
      return {"message":"Usuário não encontrado"}
    
  @userController.get("/token")
  def login(token: str = Depends(oauth2_scheme)):
    print(token)
    payload = verify_token(token)
    if not payload:
      raise HTTPException(status_code=401, detail="Token inválido ou expirado")
      
    user = user_service.get_user_by_email(email=payload["sub"])
    return {"message": "Deu boa", "user": user}
  