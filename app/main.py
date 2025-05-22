from fastapi import FastAPI
from app.config.configuration import configure_all
from app.controller.user_controller import userController
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
configure_all()

app.include_router(router=userController)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8092, reload=True, log_level="info")