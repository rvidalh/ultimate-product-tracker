from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from app.models.auth.models import User  # noqa F401
