from fastapi import FastAPI
from app.config.configuration import configure_all
from app.controller.user_controller import userController
import uvicorn

app = FastAPI()
configure_all()

app.include_router(router=userController)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True, log_level="debug")