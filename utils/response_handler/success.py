class Success:
    __RESPONSE_BODY = {
        "status": "success",
        "success": {
           
        }
    }
    
    def __init__(self) -> None:
        self.code = int()
        self.message = str()
        


    @property        
    def response(self) -> dict:
        return self.__RESPONSE_BODY
    
    def created(self):
        self.__RESPONSE_BODY["success"].clear()
        self.code = 201
        self.message = f"Successfully created"
        self.__RESPONSE_BODY["success"]["message"] = self.message
        self.__RESPONSE_BODY["success"]["code"] = self.code
        return self
    
    def updated(self):
        self.__RESPONSE_BODY["success"].clear()
        self.code = 200
        self.message = f"Successfully updated"
        self.__RESPONSE_BODY["success"]["message"] = self.message
        self.__RESPONSE_BODY["success"]["code"] = self.code
        return self
    
    def deleted(self):
        self.__RESPONSE_BODY["success"].clear()
        self.code = 200
        self.message = f"Successfully deleted"
        self.__RESPONSE_BODY["success"]["message"] = self.message
        self.__RESPONSE_BODY["success"]["code"] = self.code
        return self
    
    def results(self, *args):
        self.code = 200
        self.__RESPONSE_BODY["success"].clear()
        self.__RESPONSE_BODY["success"]["code"] = self.code
        self.__RESPONSE_BODY["success"]["results"] = list(args)
        return self