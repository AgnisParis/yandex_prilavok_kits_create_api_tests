import pytest

import data
import sender_stand_request
from random_user import RandomUser


class TestClass:

    @pytest.fixture(scope="class")
    def gen_auth_token(self):
        """
        Фикстура генерации токена авторизации. Применяется 1 раз для всех тестов

        :return: Токен авторизации
        """
        new_user = RandomUser()
        body = new_user.__dict__()
        response = sender_stand_request.post_new_user(body)
        return response.json()[data.User.AUTH_TOKEN]

    @pytest.fixture(scope="function")
    def new_kit_card_name(self, request):
        return request.param

    @staticmethod
    def __mod_kit_body(card_name):
        """
        Метод для изменения тела создаваемого набора

        :param card_name: Имя набора (обязательный параметр)
        :return: Измененное тело набора
        """
        new_kit_body = data.kit_body.copy()
        new_kit_body[data.Kit.NAME] = card_name
        return new_kit_body

    @pytest.mark.parametrize("new_kit_card_name", [
        pytest.param(
            data.CardName.OF_1_LETTER,
            id="Allowed number of characters in the card name (1)"
        ),
        pytest.param(
            data.CardName.OF_511_LETTERS,
            id="Allowed number of characters in the card name (511)"
        ),
        pytest.param(
            data.CardName.OF_512_LETTERS,
            id="Allowed number of characters in the card name (512)"
        )

    ], indirect=True)
    def test_positive_assert(self, gen_auth_token, new_kit_card_name):
        body = self.__mod_kit_body(new_kit_card_name)
        response = sender_stand_request.post_new_client_kit(gen_auth_token, body)

        assert response.status_code == 201

        assert response.json()[data.Kit.NAME] == new_kit_card_name

        print(response.json(), gen_auth_token)

    # def test_create_kit_1_letter_in_name_get_success_response(self, gen_auth_token, default_kit_body):
    #     self.positive_assert(gen_auth_token, default_kit_body, "a")
    #
    # def test_create_kit_511_letters_in_name_get_success_response(self, gen_auth_token, default_kit_body):
    #     self.positive_assert(gen_auth_token, default_kit_body, "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
    #                                                            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
    #                                                            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    #                                                            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    #                                                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
    #                                                            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
    #                                                            "cdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabc"
    #                                                            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    #                                                            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
    #                                                            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
    #                                                            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    #                                                            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
