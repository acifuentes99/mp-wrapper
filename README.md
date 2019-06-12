# MP-Wrapper

Librería para Python, que encapsula métodos de la API de Mercado Pago para "Web Tokenize Checkout" y "API".

## Motivación

Dentro de Mercado Pago existe un wrapper para Python, pero este solamente funciona para el modo "Web Checkout". Bajo la necesidad de encapsular los procedimientos de API de pago para las mencionadas en la descripción, es que se crea esta librera.

## Uso

Actualmente se disponen de dos clases, lo suficientemente necesarias para realizar pagos a través de MercadoPago:

* mpPayments("Access token") : Librería para realizar y manipular pagos
* mpCustomers("Access token") : Librería para manejo de Clientes guardados en Mercado Pago

Para usar en aplicación, se tiene que importar estas clases desde Python, y luego iniciar un objeto con el Access Token del desarrollador:

```
from mp-wrapper import mpPayments, mpCustomers

mppayments = mpPayments("access token")
mpcustomers = mpCustomers("access token")
```

Posterior a ello, puede realizarse llamadas de API.

## Métodos disponibles

### mpPayments

* create(data) : Crea un método de pago, con la información definida en documentación MercadoPago

### mpCustomers

* create(data) : Crea un Costumer en MercadoPago
* search(data) : Busca información de un Customer en particular. Útil para rescatar datos de tarjeta.
* card_create(data) : Crea una tarjeta para un Customer
