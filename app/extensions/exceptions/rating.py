from http import HTTPStatus

from app.extensions.api_codes import APICode
from app.extensions.exceptions import APIException


class RatingNotSaveException(APIException):
    code = APICode.NOT_SAVE_RATING
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, message=code.description,
                 extra=None):
        self.message = message
        self.extra = extra


class RatingSuccessCreate(APIException):
    code = APICode.SUCCESS_CREATE_RATING
    http_status = HTTPStatus.OK

    def __init__(self, message=code.description,
                 extra=None):
        self.message = message
        self.extra = extra


class RatingNotFoundException(APIException):
    code = APICode.RATING_NOT_FOUND
    http_status = HTTPStatus.NOT_FOUND

    def __init__(self, message=APICode.RATING_NOT_FOUND.description,
                 extra=None):
        self.message = message
        self.extra = extra
