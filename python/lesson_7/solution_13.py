import json

class ParsesCookies:
    def cookies(self):
        return self.request["cookies"]  

    def is_authed(self):
        return "auth_key" in self.request["cookies"] 

class ParsesBody:
    def body(self):
        return self.request["body"]  

class ParsesHeaders:
    def headers(self):
        return self.request["headers"] 

    def need_json(self):
        return ("content-type" in self.request["headers"]) and (self.request["headers"]["content-type"] == "application/json")

class JsonHandler(ParsesBody, ParsesHeaders):
    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.need_json():
            return None

        try:
            return len(json.loads(self.body()).keys())
        except:
            return None



        

        