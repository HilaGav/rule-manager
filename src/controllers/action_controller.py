from flask_restx import Api, Namespace, Resource
from src.common.models.rule import Rule


api = Api(version='1.0', title='API manager', description='')
ns = Namespace('rule', description='manage action')
api.add_namespace(ns)


@api.route('/action/create')
class CreateAction(Resource):
    @api.doc(responses={200: 'Success', 500: 'Internal Server Error'})
    def put(self, rule: Rule):
        return {'message': 'New hello message created!'}

