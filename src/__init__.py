from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.logic.db.rule_provider import RuleProvider

db = SQLAlchemy()
db_logics = RuleProvider(db)


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from .controllers import rule_controller

        db.create_all()
        db_logics = RuleProvider(db)
        return app
