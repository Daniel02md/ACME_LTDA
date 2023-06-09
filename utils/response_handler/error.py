class Error:
    __RESPONSE_BODY = {
        "status": "error",
        "error": {
           
        }
    }
    
    def __init__(self) -> None:
        self.code = int()
        self.message = str()
        


    @property        
    def response(self) -> dict:
        return self.__RESPONSE_BODY
    
    def invalid_values(self, *args):
        self.code = 422
        self.message = f"Invalid Values"
        self.__RESPONSE_BODY["error"]["message"] = self.message
        self.__RESPONSE_BODY["error"]["code"] = self.code
        self.__RESPONSE_BODY["error"]["items"] = list(args)
        return self
    
    def does_not_exist(self, *args):
        self.code = 404
        self.message = f"Does not exists"
        self.__RESPONSE_BODY["error"]["message"] = self.message
        self.__RESPONSE_BODY["error"]["code"] = self.code
        self.__RESPONSE_BODY["error"]["items"] = list(args)
        return self
    
    def conflict(self, *args):
        self.code = 409
        self.message = f"Already exists"
        self.__RESPONSE_BODY["error"]["message"] = self.message
        self.__RESPONSE_BODY["error"]["code"] = self.code
        self.__RESPONSE_BODY["error"]["items"] = list(args)
        return self
        
    def null_value(self, *args):
        self.code = 400
        self.message = f"Null value"
        self.__RESPONSE_BODY["error"]["message"] = self.message
        self.__RESPONSE_BODY["error"]["code"] = self.code
        self.__RESPONSE_BODY["error"]["items"] = list(args)
        return self
    

