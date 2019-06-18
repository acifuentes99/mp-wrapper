import json
import requests

class MercadoPagoClass:
    API_BASE_URL = "https://api.mercadopago.com"
    MIME_JSON = "application/json"
    MIME_FORM = "application/x-www-form-urlencoded"
    def __init__(self, access_token):
        self.access_token = access_token

    def post(self, url, data):
        try:
            req = requests.post(self.API_BASE_URL+url+'/?access_token='+self.access_token, json=data, headers={'Content-type':self.MIME_JSON, 'Accept':self.MIME_JSON})
            if req.ok:
                return req.json()
            else:
                return None
        except requests.exceptions.HTTPError as err:
            return None

    def get(self, url, data):
        try:
            req = requests.get(self.API_BASE_URL+url+'/?access_token='+self.access_token, params=data, headers={'Content-type':self.MIME_JSON, 'Accept':self.MIME_JSON})
            if req.ok:
                return req.json()
            else:
                return None
        except requests.exceptions.HTTPError as err:
            return None


class mpPayments(MercadoPagoClass):
    def __init__(self, access_token):
        self.access_token = access_token

    def create(self, data):
        return self.post('/v1/payments', data)


class mpCustomers(MercadoPagoClass):
    def __init__(self, access_token):
        self.access_token = access_token

    def create(self, data):
        return self.post('/v1/customers', data)

    def search(self, data):
        return self.get('/v1/customers/search', data)

    def card_create(self, data):
        return self.post('/v1/customers/'+data['customer']+'/cards', data)
