from .error import Error
from .success import Success
class Response:



    def __init__(self) -> None:
        pass

    @property
    def success(self) -> Success:
        return Success()
    

    @property
    def error(self) -> Error:
        return Error()