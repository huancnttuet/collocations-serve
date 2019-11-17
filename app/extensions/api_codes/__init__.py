from enum import Enum


class APICode(str, Enum):
    """
    API codes and descriptions

    Basic format `US{xxx}{D|E|S}`:
        - Prefixes:
            - `USI` stands for `User Service API`
        - Suffixes:
            - `D`: Default suffix
            - `E`: Error cases
            - `S`: Success cases
    """

    def __new__(cls, value, description):
        obj = str.__new__(cls, value)
        obj._value_ = value

        obj.description = description
        return obj

    DEFAULT = ('USIA001D', 'API has no specific code for this case')

    # Success codes

    SUCCESS_CREATE_RATING = ('USI001S', 'Success Create Rating')
    SUCCESS_CREATE_CLIENT = ('USI002S', 'Success Create Client')

    SUCCESS_GET_RATING = ('USI003S', 'Success GET Rating')
    SUCCESS_GET_CLIENT = ('USI004S', 'Success GET Client')

    # Errors codes
    UNHANDLED_ERROR = ("USI001E", "This error has not been handled")

    RATING_NOT_FOUND = ("USI002E", "The requested rating can not be found")
    CLIENT_NOT_FOUND = ("USI003E", "The requested client can not be found")

    NOT_SAVE_RATING = ("USI004E", "Error when save rating")
    NOT_SAVE_CLIENT = ("USI005E", "Error when save client")
