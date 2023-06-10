from flask import request
from src import db_logics
from src.common.models.rule import Rule
from flask import current_app as app


@app.route('/rules')
def get_all_rules():
    return {'message': 'New hello message created!'}


@app.route('/rules', methods=['POST'])
def create_rule():
    rule = rule_create(request.json)
    if db_logics.insert_rule(rule):
        return 200
    return 400


@app.route('/rule/<id>', methods=['PUT'])
def edite_rule(id):
    return {'message': 'New hello message created!'}


@app.route('/rule/<id>', methods=['DELETE'])
def delete_rule(id):
    return {'message': 'New hello message created!'}


def rule_create(obj):
    return Rule(app=obj['app'], condition=obj['condition'], countries=obj['countries'], action=obj['action'])
