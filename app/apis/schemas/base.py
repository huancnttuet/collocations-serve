# coding=utf-8
from marshmallow import Schema, post_dump
from marshmallow.fields import String

from app.extensions.api_codes import APICode


class BaseResponseSchema(Schema):
    @post_dump(pass_original=True)
    def wrap(self, result, original, many, **kwargs):
        context = {}

        if isinstance(original, Schema):
            context = original.context

        return ResponseFormatter.format(result, context)


class ResponseFormatter:
    @staticmethod
    def format(result, context):
        response = {
            "code": APICode.DEFAULT,
            "message": APICode.DEFAULT.description,
            "result": result
        }

        if context.get('code'):
            response['code'] = context.get('code')

        if context.get('message'):
            response['message'] = context.get('message')

        if context.get('extra'):
            response['extra'] = context.get('extra')

        return response
