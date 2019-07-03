from .base import MercadoPagoClass


class Payments(MercadoPagoClass):
    def create(self, data):
        return self.post('/v1/payments', data)

    def get(self, payment_id):
        return self.get('/v1/payments/'+str(payment_id))

    def put(self, payment_id, data):
        return self.post('/v1/payments/'+str(payment_id), data)

    def search(self, data):
        return self.get('/v1/payments', data)


class Customers(MercadoPagoClass):
    def __init__(self, access_token):
        self.access_token = access_token
        self.cards = Cards(access_token)

    def create(self, data):
        return self.post('/v1/customers', data)

    def search(self, data):
        return self.get('/v1/customers/search', data)


class Cards(MercadoPagoClass):
    def create(self, data):
        return self.post('/v1/customers/'+data['customer']+'/cards', data)

    def delete(self, customer_id, card_id):
        return self.delete('/v1/customers/'+str(customer_id)+'/cards/'+str(card_id))
