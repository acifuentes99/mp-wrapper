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
        try:
            req = requests.post(self.API_BASE_URL+url+'/?access_token='+self.access_token, json=data, headers=self.headers)
            if req.ok:
                return req.json()
            else:
                raise Exception(req.text)
        except requests.exceptions.HTTPError as err:
            return err

    def get(self, url, data=None):
        try:
            if data:
                req = requests.get(self.API_BASE_URL+url+'/?access_token='+self.access_token, params=data, headers=self.headers)
            else:
                req = requests.get(self.API_BASE_URL+url+'/?access_token='+self.access_token, headers=self.headers)
            if req.ok:
                return req.json()
            else:
                raise Exception(req.text)
        except requests.exceptions.HTTPError as err:
            return err

    def put(self, url, data):
        try:
            req = requests.post(self.API_BASE_URL+url+'/?access_token='+self.access_token, json=data, headers=self.headers)
            if req.ok:
                return req.json()
            else:
                raise Exception(req.text)
        except requests.exceptions.HTTPError as err:
            return err

    def delete(self, url, data=None):
        try:
            req = requests.delete(self.API_BASE_URL+url+'/?access_token='+self.access_token, headers=self.headers)
            if req.ok:
                return req.json()
            else:
                raise Exception(req.text)
        except requests.exceptions.HTTPError as err:
            return err
