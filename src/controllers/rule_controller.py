from flask_restx import Api, Namespace, Resource
from src.common.models.rule import Rule


api = Api(version='1.0', title='API manager', description='')
ns = Namespace('rule', description='manage rules')
api.add_namespace(ns)


@api.route('/rule/create')
class CreateRule(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def post(self, rule: Rule):
        return {'message': 'New hello message created!'}


@api.route('/rule/edit')
class EditeRule(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def put(self, rule: Rule):
        return {'message': 'New hello message created!'}


@api.route('/rule/delete')
class EditeRule(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def delete(self, rule: Rule):
        return {'message': 'New hello message created!'}


@api.route('/rule/get_all')
class EditeRule(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def get(self):
        return {'message': 'New hello message created!'}


@api.route('/action/create')
class CreateAction(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def post(self, rule: Rule):
        return {'message': 'New hello message created!'}