from fastapi import FastAPI
from app.config.configuration import configure_all
from app.controller.user_controller import userController

app = FastAPI()
configure_all()

app.include_router(router=userController)
