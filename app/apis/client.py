from flask_accepts import responds, accepts
from flask_restplus import Resource, Namespace
from flask import request

from app.apis.schemas.common import IdOnlySchema
from app.apis.schemas.client import ClientCreateSchema
from app.extensions.api_codes import APICode
from app.services.client import ClientService

api = Namespace('Clients')


@api.route('/', methods=['POST'])
class Clients(Resource):
    @accepts(model_name="Client", schema=ClientCreateSchema, api=api)
    @responds(schema=IdOnlySchema, status_code=201)
    def post(self):
        data = request.args or request.json or request.form
        response = ClientService.create_client(data)

        schema = IdOnlySchema()
        schema.id = response.id
        schema.context = {
            'code': APICode.SUCCESS_CREATE_CLIENT,
            'message': APICode.SUCCESS_CREATE_CLIENT.description
        }

        return schema


@api.route('/<string:client_id>', methods=['GET'])
class Client(Resource):
    @responds(schema=IdOnlySchema)
    def get(self, client_id):
        response = ClientService.get_by_id(client_id)
        schema = IdOnlySchema()
        schema.id = response.id
        schema.context = {
            'code': APICode.SUCCESS_GET_CLIENT,
            'message': APICode.SUCCESS_GET_CLIENT.description
        }

        return schema
