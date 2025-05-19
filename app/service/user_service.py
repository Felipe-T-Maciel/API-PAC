from app.models.DTO.user.UserPostDTO import UserPostDTO
from app.models.User import User
from app.config.database import SessionLocal
import bcrypt

class User_service():
  
  def __init__(self):
     db = SessionLocal()
     self.db = db
     
  def create_user(self, user: UserPostDTO):
    encode_pass = self.encode_pass(user.password)
    
    new_user = User(
      password=encode_pass,
      email = user.email
    )
    self.db.add(new_user)
    self.db.commit()
    self.db.refresh(new_user)
    return new_user
  
  def login(self, email:str, password:str):
    user = self.get_user_by_email(email)
    
    if not user:
      return None
    
    if not self.verify_pass(user.password, password):
      return None
    
    return user
  
  def update_user(self, user_id: int, user_data: UserPostDTO):
    user = self.get_user_by_id(user_id)
    
    if not user:
        return None
    
    for key, value in vars(user_data).items():
      if value is not None:
        setattr(user, key, value)
    
    if user_data.password:
        user.password = self.encode_pass(user_data.password)
    
    self.db.commit()
    self.db.refresh(user)
    
    return user
  
  @staticmethod
  def encode_pass(password:str) -> str:
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass.decode('utf-8')
  
  @staticmethod
  def verify_pass(stored_hash:str, password:str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
  
  def get_user_by_email(self, email:str):
    return self.db.query(User).filter(User.email == email).first()
  
  def get_user_by_id(self, user_id:int):
    return self.db.query(User).filter(User.id == user_id).first()
  
  def delete_user(self, user_id:int) -> str:
    user = self.get_user_by_id(user_id)
    if not user:
      return None
    self.db.delete(user)
    self.db.commit()
    return "Usuário deletado com sucesso"
  