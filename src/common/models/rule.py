from src import db


class Rule(db.Model):
    app = db.Column(db.Text)
    condition = db.Column(db.Integer, primary_key=True)
    countries = db.Column(db.Text)
    action = db.Column(db.Integer, unique=True, nullable=False)
