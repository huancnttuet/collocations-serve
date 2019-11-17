import pprint

from flask_accepts import responds, accepts
from flask_restplus import Resource, Namespace
from flask import request
from flask_cors import cross_origin

from app.apis.schemas.common import IdOnlySchema
from app.apis.schemas.uploadfile import UploadFileCreateSchema, UploadFileResponseSchema
from app.extensions.api_codes import APICode
from app.services.uploadfile import UploadFileService
from app.tasks.celery import run_tasks

api = Namespace('Upload File')


@api.route('/', methods=['POST'])
@cross_origin()
class UploadFile(Resource):
    @accepts(model_name="UploadFile", schema=UploadFileCreateSchema, api=api)
    @responds(schema=IdOnlySchema, status_code=201)
   
    def post(self):
        data = request.args or request.json or request.form
        print(data)
        response = UploadFileService.create_file(data)

        schema = IdOnlySchema()
        schema.id = response.id
        schema.context = {
            'code': APICode.SUCCESS_CREATE_RATING,
            'message': APICode.SUCCESS_CREATE_RATING.description
        }

        return schema


@api.route('/<string:rating_id>', methods=['GET'])
class UploadFile(Resource):
    @responds(schema=IdOnlySchema)
    def get(self, rating_id):
        response = UploadFileService.get_by_id(rating_id)
        result = run_tasks.delay()
        print('Task data')
        print(result)

        schema = IdOnlySchema()
        schema.id = response.id
        schema.context = {
            'code': APICode.SUCCESS_GET_RATING,
            'message': APICode.SUCCESS_GET_RATING.description
        }

        return schema
