from app.config.database import engine, Base
from app.models.User import User # type: ignore


def configure_all():
  Base.metadata.create_all(bind=engine)