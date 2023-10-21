import configuration
import requests
import data
from random_user import RandomUser


def post_new_user(body=RandomUser().get_json()):
    return requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_USER_PATH}",  # подставляем полный url
        json=body,  # тут тело
        headers=data.headers  # а здесь заголовки
    )


def post_new_client_kit(auth_token, body):
    return requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_KIT_PATH}",
        json=body,
        headers=data.headers,
        auth=auth_token
    )