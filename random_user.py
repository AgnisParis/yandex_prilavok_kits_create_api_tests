import random
import string
import json

from mimesis import Person, Address
from mimesis.locales import Locale


class RandomUser:
    def __init__(
            self,
            name=None,
            phone=None,
            address=None,
            email=None,
            comment=None
    ):
        self.__name = name if name else self.__gen_random_name()

        self.__phone = phone if phone else self.__gen_random_phone()

        self.__address = address if address else self.__gen_random_address()

        self.__email = email if email else self.__gen_random_email()

        self.__comment = comment if comment else self.__gen_random_comment(23)

    @staticmethod
    def __gen_random_name():
        return Person(Locale.RU).name()

    @staticmethod
    def __gen_random_phone():
        return f"+7{''.join(random.choices(string.digits, k=10))}"

    @staticmethod
    def __gen_random_address():
        return Address(Locale.RU).address()

    @staticmethod
    def __gen_random_email():
        return Person(Locale.RU).email()

    @staticmethod
    def __gen_random_comment(length):
        a = ord('а')  # Russian alphabet first letter char code
        rus_alphabet = ''.join(
            [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        )
        valid_chars = f"{rus_alphabet}{rus_alphabet.upper()}{string.punctuation} {string.digits}"

        return ''.join(random.choices(valid_chars, k=length))

    def __dict__(self, is_full=False):
        dict = {"firstName": self.__name, "phone": self.__phone, "address": self.__address}
        if is_full:
            pass

    def __str__(self, is_full=False):
        return f"{self.__name}\n{self.__phone}\n{self.__address}"


user = RandomUser()
user1 = RandomUser("alex", "+79001234567")

print(vars(user))
print(user1)
print(user)