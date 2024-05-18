import os

# app의 config를 작성


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATE_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "templates"
    )
    STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
