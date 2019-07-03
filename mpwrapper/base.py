import json
import requests

class MercadoPagoClass:
    API_BASE_URL = "https://api.mercadopago.com"
    MIME_JSON = "application/json"
    MIME_FORM = "application/x-www-form-urlencoded"
    headers = {'Content-type': MIME_JSON, 'Accept': MIME_JSON}

    def __init__(self, access_token):
        self.access_token = access_token

    def post(self, url, data):
        req = requests.post(self.API_BASE_URL+url+'/?access_token='+self.access_token, json=data, headers=self.headers)
        return {
            'status': True if req.ok else False,
            'response': req.json()
        }

    def get(self, url, data=None):
        if data:
            req = requests.get(self.API_BASE_URL+url+'/?access_token='+self.access_token, params=data, headers=self.headers)
        else:
            req = requests.get(self.API_BASE_URL+url+'/?access_token='+self.access_token, headers=self.headers)
        return {
            'status': True if req.ok else False,
            'response': req.json()
        }

    def put(self, url, data):
        req = requests.post(self.API_BASE_URL+url+'/?access_token='+self.access_token, json=data, headers=self.headers)
        return {
            'status': True if req.ok else False,
            'response': req.json()
        }

    def delete(self, url, data=None):
        req = requests.delete(self.API_BASE_URL+url+'/?access_token='+self.access_token, headers=self.headers)
        return {
            'status': True if req.ok else False,
            'response': req.json()
        }
