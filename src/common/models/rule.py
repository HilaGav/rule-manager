from src import db


class Rule(db.Model):
    __tablename__ = "rules"
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.Text)
    rule_name = db.Column(db.Text, unique=True, nullable=False)
    condition = db.Column(db.Integer)
    countries = db.Column(db.Text)
    action = db.Column(db.Integer, nullable=False)
