from flask import request
from src.common.models.rule import Rule
from src import db
from flask import current_app as app
from src.logic.db.rule_provider import RuleProvider


@app.route('/rule')
def get_all_rules():
    return {'message': 'New hello message created!'}


@app.route('/rule', methods=['POST'])
def create_rule():
    rule = rule_create(request.json)
    if RuleProvider.insert_rule(db, rule):
        return "Succeeded create rule", 200
    return "Failed create rule", 500


@app.route('/rule/<name>', methods=['PUT'])
def edite_rule(name):
    return {'message': 'New hello message created!'}


@app.route('/rule/<name>', methods=['DELETE'])
def delete_rule(name):
    return {'message': 'New hello message created!'}


def rule_create(obj):
    return Rule(id=obj['id'], rule_name=obj['rule_name'], app=obj['app'], condition=obj['condition'], countries=obj['countries'], action=obj['action'])
