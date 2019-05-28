import requests

class Request:
    def get(self, url: str): 
        response = requests.get(url)

Request().get('https://api.github.com')