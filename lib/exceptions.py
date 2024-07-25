from dataclasses import dataclass


@dataclass(frozen=True)
class DirectorioBaseException(Exception):
    """
    Abstract base class for exceptions. Should not be thrown directly.
    Please use one of the below subclasses or create a new one only if
        it requires special treatment.
    Fields:
        message: Human-readable description of the error.
        status_code: HTTP status code for the response
    """

    message: str
    http_status_code: int = 500


@dataclass(frozen=True)
class TokenException(DirectorioBaseException):
    """
    Exception raised when get auth token
    """

    def __init__(self, message: str = "Unexpected empty entity"):
        super().__init__(
            message=message,
            http_status_code=422,
        )
