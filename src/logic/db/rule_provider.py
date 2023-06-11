from flask_sqlalchemy import SQLAlchemy
from src.common.models.rule import Rule


class RuleProvider:
    @staticmethod
    def insert_rule(db: SQLAlchemy, rule: Rule):
        if rule is None:
            return False
        db.session.add(rule)
        db.session.commit()
        return True

    @staticmethod
    def update_rule(db: SQLAlchemy, new_rule: Rule, rule_name):
        if new_rule is None:
            return False
        db.session.query(Rule.rule_name is rule_name).update(new_rule)
        db.session.commit()
        return True
