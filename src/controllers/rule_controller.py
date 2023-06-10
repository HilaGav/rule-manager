import json

from flask import request
from src.common.models.rule import Rule, db
from flask import current_app as app


@app.route('/rule/get_all')
def get_all_rules():
    return {'message': 'New hello message created!'}


@app.route('/rule/create', methods=['POST'])
def create_rule():
    rule = rule_create(request.json)
    db.session.add(rule)
    db.session.commit()
    return {'message': 'New hello message created!'}


@app.route('/rule/edit', methods=['PUT'])
def edite_rule():
    return {'message': 'New hello message created!'}


@app.route('/rule/delete', methods=['DELETE'])
def delete_rule():
    return {'message': 'New hello message created!'}


def rule_create(obj):
    return Rule(app=obj['app'], condition=obj['condition'], countries=obj['countries'], action=obj['action'])
