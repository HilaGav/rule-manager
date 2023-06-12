from flask import current_app as app
from flask import request
from src import db
from src.common.models.rule import Rule
from src.logic.db.rule_manager import RulesManager

rule_manager = RulesManager(db)


@app.route('/rules')
def get_all_rules():
    return {'message': 'New hello message created!'}


@app.route('/rules', methods=['POST'])
def create_rule():
    rule = rule_create(request.json)
    if rule_manager.insert_rule(rule):
        return "Succeeded create rule", 200
    return "Failed create rule", 500


@app.route('/rules/<name>', methods=['PUT'])
def edite_rule(name):
    rule = rule_create(request.json)
    rule_manager.update_rule(rule, name)
    return {'message': 'New hello message created!'}


@app.route('/rules/<name>', methods=['DELETE'])
def delete_rule(name):
    return {'message': 'New hello message created!'}


def rule_create(obj):
    return Rule(id=obj['id'], rule_name=obj['rule_name'], app=obj['app'], condition=obj['condition'],
                countries=obj['countries'], action=obj['action'])
