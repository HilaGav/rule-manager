from flask_sqlalchemy import SQLAlchemy
from src.common.models.rule import Rule


class RuleProvider:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def insert_rule(self, rule: Rule):
        if rule is None:
            return False
        self.db.session.add(rule)
        self.db.session.commit()
        return True
