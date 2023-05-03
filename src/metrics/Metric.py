class Metric:

    def __init__(self, name, payload: dict):
        self.name = name
        self.payload = payload


    def get_name(self) -> str:
        return self.name
    
    def get_payload(self) -> dict:
        return self.payload