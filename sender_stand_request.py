import requests

import configuration
import data


def post_new_user(body):
    return requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_USER_PATH}",  # подставляем полный url
        json=body,  # тут тело
        headers=data.headers  # а здесь заголовки
    )


def post_new_client_kit(auth_token, body):
    auth_header = data.kit_auth_header.copy()
    auth_header["authToken"] = auth_token

    return requests.post(
        url=f"{configuration.URL_SERVICE}{configuration.CREATE_KIT_PATH}",
        json=body,
        headers=data.headers | auth_header
    )
