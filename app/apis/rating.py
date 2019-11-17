import pprint

from flask_accepts import responds, accepts
from flask_restplus import Resource, Namespace
from flask import request

from app.apis.schemas.common import IdOnlySchema
from app.apis.schemas.rating import RatingCreateSchema, RatingResponseSchema
from app.extensions.api_codes import APICode
from app.services.rating import RatingService
from app.tasks.celery import run_tasks

api = Namespace('Ratings')


@api.route('/', methods=['POST'])
class Ratings(Resource):
    @accepts(model_name="Rating", schema=RatingCreateSchema, api=api)
    @responds(schema=IdOnlySchema, status_code=201)
    def post(self):
        data = request.args or request.json or request.form
        response = RatingService.create_rating(data)

        schema = IdOnlySchema()
        schema.id = response.id
        schema.context = {
            'code': APICode.SUCCESS_CREATE_RATING,
            'message': APICode.SUCCESS_CREATE_RATING.description
        }

        return schema


@api.route('/<string:rating_id>', methods=['GET'])
class Rating(Resource):
    @responds(schema=IdOnlySchema)
    def get(self, rating_id):
        response = RatingService.get_by_id(rating_id)
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
