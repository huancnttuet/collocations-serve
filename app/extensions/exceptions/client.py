from http import HTTPStatus

from app.extensions.api_codes import APICode
from app.extensions.exceptions import APIException


class ClientNotSaveException(APIException):
    code = APICode.NOT_SAVE_CLIENT
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, message=code.description,
                 extra=None):
        self.message = message
        self.extra = extra


class ClientSuccessCreate(APIException):
    code = APICode.SUCCESS_CREATE_CLIENT
    http_status = HTTPStatus.OK

    def __init__(self, message=code.description,
                 extra=None):
        self.message = message
        self.extra = extra


class ClientNotFoundException(APIException):
    code = APICode.CLIENT_NOT_FOUND
    http_status = HTTPStatus.NOT_FOUND

    def __init__(self, message=APICode.CLIENT_NOT_FOUND.description,
                 extra=None):
        self.message = message
        self.extra = extra
