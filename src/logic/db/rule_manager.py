from flask_sqlalchemy import SQLAlchemy
from src.common.models.rule import Rule
from src.common.models.rule_entity import RuleEntity


class RulesManager:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def insert_rule(self, rule: Rule):
        if rule is None:
            return False

        self.db.session.add(self.rule_to_rule_entity(rule))
        self.db.session.commit()
        return True

    def update_rule(self, new_rule: Rule, id):
        if new_rule is None:
            return False
        self.db.session.commit()
        return True

    @staticmethod
    def rule_to_rule_entity(rule: Rule) -> RuleEntity:
        return RuleEntity(id=rule.id, rule_name=rule.rule_name, app=rule.app, condition=rule.condition,
                          countries=rule.countries, action=rule.action)
