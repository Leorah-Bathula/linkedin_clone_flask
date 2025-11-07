import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey123")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Jessi03*@localhost/linkedin_clone"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
