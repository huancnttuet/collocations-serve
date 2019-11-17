from http import HTTPStatus
from app.extensions.exceptions import APIException
from app.extensions.api_codes import APICode


def register_error_handler(app):
    # TODO: Log exception and notify engineers
    app.register_error_handler(Exception, application_error_handler)


def application_error_handler(e):
    if isinstance(e, APIException):
        return api_error_handler(e)
    else:
        return unknown_error_handler(e)


def api_error_handler(e):
    response = {
        "code": e.code,
        "message": e.code.description,
    }

    if e.message is not None:
        response["message"] = e.message

    if e.extra is not None:
        response["extra"] = e.extra

    return response, e.http_status


def unknown_error_handler(e):
    response = {
        "code": APICode.UNHANDLED_ERROR,
        "message": APICode.UNHANDLED_ERROR.description,
        "extra": {
            "original_error": str(e)
        }
    }

    return response, HTTPStatus.INTERNAL_SERVER_ERROR
