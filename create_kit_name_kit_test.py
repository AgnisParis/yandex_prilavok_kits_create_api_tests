import sender_stand_request
import data
from random_user import RandomUser


class TestClass:

    def __init__(self, auth_token=None):
        self.__auth_token = auth_token if auth_token else self.__gen_new_user_token()

    @staticmethod
    def __gen_new_user_token():
        new_user = RandomUser()
        body = new_user.get_json()
        response = sender_stand_request.post_new_user(body)
        return response.json()["authToken"]

    @staticmethod
    def __mod_json_value(cur_json, key, new_val):
        new_json = cur_json.copy()
        if key in new_json:
            new_json[key] = new_val
        return new_json

    def positive_assert(kit_body):
        pass
