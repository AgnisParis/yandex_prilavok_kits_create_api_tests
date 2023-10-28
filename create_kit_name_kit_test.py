import pytest

import data
import sender_stand_request
from random_user import RandomUser


class TestClass:

    @pytest.fixture(scope="class")
    def gen_auth_token(self):
        """
        Фикстура генерации токена авторизации. Применяется 1 раз для всех тестов класса

        :return: Токен авторизации
        """
        new_user = RandomUser()
        body = new_user.__dict__()
        response = sender_stand_request.post_new_user(body)
        return response.json()[data.User.AUTH_TOKEN]

    @pytest.fixture(scope="function")
    def gen_new_kit_body(self, request):
        """
        Фикстура генерации тела запроса. Тело запроса для каждого теста меняется в зависимости от параметра

        :param request: Имя набора (изменяется для каждого теста)
        :return: Обновленное тело запроса (с измененным именем набора)
        """
        new_kit_body = data.kit_body.copy()
        if request.param:
            new_kit_body[data.Kit.NAME] = request.param
        else:
            new_kit_body.pop(data.Kit.NAME)
        return new_kit_body

    @pytest.mark.parametrize("gen_new_kit_body", [
        pytest.param(
            data.CardName.OF_1_LETTER,
            marks=[pytest.mark.positive],
            id="Allowed number of characters in the card name (1)"
        ),
        pytest.param(
            data.CardName.OF_511_LETTERS,
            marks=[pytest.mark.positive],
            id="Allowed number of characters in the card name (511)"
        ),
        pytest.param(
            data.CardName.OF_ENGLISH_LETTERS,
            marks=[pytest.mark.positive],
            id="Allowed English alphabet characters in the card name"
        ),
        pytest.param(
            data.CardName.OF_RUSSIAN_LETTERS,
            marks=[pytest.mark.positive],
            id="Allowed Russian alphabet of characters in the card name"
        ),
        pytest.param(
            data.CardName.OF_WILDCARDS,
            marks=[pytest.mark.positive],
            id="Allowed wildcards characters in the card name"
        ),
        pytest.param(
            data.CardName.OF_WHITESPACES_AND_LETTERS,
            marks=[pytest.mark.positive],
            id="Allowed spaces in the card name"
        ),
        pytest.param(
            data.CardName.OF_DIGITS,
            marks=[pytest.mark.positive],
            id="Allowed digits in the card name"
        )
    ], indirect=True)
    def test_positive_assert(self, gen_auth_token, gen_new_kit_body):
        response = sender_stand_request.post_new_client_kit(gen_auth_token, gen_new_kit_body)

        assert response.status_code == 201

        assert response.json()[data.Kit.NAME] == gen_new_kit_body[data.Kit.NAME]

    @pytest.mark.parametrize("gen_new_kit_body", [
        pytest.param(
            data.CardName.OF_0_LETTER,
            marks=[pytest.mark.negative, pytest.mark.xfail],
            id="Number of characters in the card name is less than allowed number of characters (0)"
        ),
        pytest.param(
            data.CardName.OF_512_LETTERS,
            marks=[pytest.mark.negative, pytest.mark.xfail],
            id="Number of characters in the card name is greater than allowed number of characters (512)"
        ),
        pytest.param(
            data.CardName.OF_ANOTHER_TYPE,
            marks=[pytest.mark.negative, pytest.mark.xfail],
            id="Passed a different type of parameter (number) to the card name"
        ),
        pytest.param(
            data.CardName.OF_NONE,
            marks=[pytest.mark.negative, pytest.mark.xfail],
            id="Card name parameter is not passed in the request"
        )
    ], indirect=True)
    def test_negative_assert_code_400(self, gen_auth_token, gen_new_kit_body):
        response = sender_stand_request.post_new_client_kit(gen_auth_token, gen_new_kit_body)

        assert response.status_code == 400
