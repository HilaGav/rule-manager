from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = 'YOURSECRETKEY'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\User\\PycharmProjects\\rule-manager\\test.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
