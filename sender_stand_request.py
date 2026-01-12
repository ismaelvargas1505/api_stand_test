import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_product_kits(product_ids):
    return requests.post(configuration.URL_SERVICE+ configuration.PRODUCTS_KITS_PATHS,
                         json= product_ids,
                         headers=data.headers)
response =post_product_kits (data.product_ids); 
print(response.status_code)
print(response.json())