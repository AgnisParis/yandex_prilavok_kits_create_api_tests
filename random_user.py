import random
import string
import json

from mimesis import Person, Address
from mimesis.locales import Locale


class RandomUser:
    def __init__(
            self,
            name=None,
            email=None,
            phone=None,
            comment=None,
            address=None
    ):
        self.__name = name if name else self.__gen_random_name()

        self.__email = email if email else self.__gen_random_email()

        self.__phone = phone if phone else self.__gen_random_phone()

        self.__comment = comment if comment else self.__gen_random_comment(23)

        self.__address = address if address else self.__gen_random_address()

    @staticmethod
    def __gen_random_name():
        return Person(Locale.RU).name()

    @staticmethod
    def __gen_random_email():
        return Person(Locale.RU).email()

    @staticmethod
    def __gen_random_phone():
        return f"+7{''.join(random.choices(string.digits, k=10))}"

    @staticmethod
    def __gen_random_comment(length):
        """
        Создание произвольного коммента определенной длины из русских букв и спецсимволов

        :param length: Длина коммента
        :return: Произвольный коммент в виде строки
        """
        a = ord('а')  # Код первой буквы русского алфавита
        rus_alphabet = ''.join(
            [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        )
        valid_chars = f"{rus_alphabet}{rus_alphabet.upper()}{string.punctuation} {string.digits}"

        return ''.join(random.choices(valid_chars, k=length))

    @staticmethod
    def __gen_random_address():
        return Address(Locale.RU).address()

    def get_json(self, is_full=False):
        """
        Получить json с русскими символами

        :param is_full: Полное или краткое представление объекта (по умолчанию - краткое)
        :return: json структура объекта класса
        """
        return json.dumps(self.____dict__(is_full), ensure_ascii=False)

    def ____dict__(self, is_full=False):
        """
        Перегрузка представления объекта класса в виде словаря (для последующей сериализации в json)

        :param is_full: Полное или краткое представление объекта (по умолчанию - краткое)
        :return: Представление объекта класса в виде словаря
        """
        supp_k = ["email", "comment"]
        dct = {
            "firstName": self.__name,
            supp_k[0]: self.__email,
            "phone": self.__phone,
            supp_k[1]: self.__comment,
            "address": self.__address
        }
        if not is_full:
            return {k: v for k, v in dct.items() if k not in supp_k}
        return dct

    def __str__(self):
        """
        Перегруженная строка для читаемого представления объекта класса

        :return: Объект класса в виде строки
        """
        s = ""
        for key, val in self.____dict__(True).items():
            s += f"{key}: {val}\n"

        return s


user = RandomUser()
user1 = RandomUser("alex", "+79001234567")

# print(vars(user))
# print(user1.__str__(True))
print(user)
print(user1)
print(user.__dict__)
print(user1.__dict__)
print(user.get_json(True))
print(user1.get_json())
