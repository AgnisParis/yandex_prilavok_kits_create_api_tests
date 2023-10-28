from dataclasses import dataclass
from typing import ClassVar


headers = {
    "Content-Type": "application/json"
}

kit_auth_header = {
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

kit_body = {
    "name": "string"
    # "cardId": 0
}

body = {"firstName": "alex", "phone": "+73041188015", "address": "Аллея Рословка 615"}


@dataclass
class User:
    NAME: ClassVar[str] = "firstName"
    MAIL: ClassVar[str] = "email"
    PHONE: ClassVar[str] = "phone"
    COMMENT: ClassVar[str] = "comment"
    ADDRESS: ClassVar[str] = "address"
    AUTH_TOKEN: ClassVar[str] = "authToken"


@dataclass
class Kit:
    NAME: ClassVar[str] = "name"
    CARD_ID: ClassVar[str] = "cardId"


@dataclass
class CardName:
    OF_NONE: ClassVar[None] = None
    OF_ENGLISH_LETTERS: ClassVar[str] = "QWErty"
    OF_RUSSIAN_LETTERS: ClassVar[str] = "Мария"
    OF_WILDCARDS: ClassVar[str] = '"№%@",'
    OF_WHITESPACES_AND_LETTERS: ClassVar[str] = "Человек и КО "
    OF_DIGITS: ClassVar[str] = "123"
    OF_ANOTHER_TYPE: ClassVar[int] = 123
    OF_0_LETTER: ClassVar[str] = ""
    OF_1_LETTER: ClassVar[str] = "a"
    OF_511_LETTERS: ClassVar[str] = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabC")
    OF_512_LETTERS: ClassVar[str] = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcD")
