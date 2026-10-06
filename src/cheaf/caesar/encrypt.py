#!/usr/bin/env python3

from cheaf import io
from cheaf import caesar



def charSubs(plain_char: str, key: str) -> str:
    if not isinstance(plain_char, str):
        raise TypeError(f"can't use non-str of type '{type(plain_char).__name__}' as plain_char")
    elif len(plain_char) != 1:
        raise ValueError(f"'{plain_char}' need to have a lenght of 1")

    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type '{type(key).__name__}' as key")
    elif len(key) != 1:
        raise ValueError(f"'{key}' need to have a lenght of 1")

    ascii_table: dict[str:int] = io.table.getTable()
    ascii_values: tuple[str] = tuple(ascii_table.keys())

    cipher_index: int = (ascii_table[plain_char] - 32 + ascii_table[key] - 32) % len(ascii_table)

    return ascii_values[cipher_index]


def plainSubs(plain: str, key: str, encryption: str) -> str:
    if not isinstance(plain, str):
        raise TypeError(f"can't use non-str of type {type(plain).__name__} as plain")

    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type {type(key).__name__} as key")

    elif not isinstance(encryption, str):
        raise TypeError(f"can't use non-str of type {type(encryption).__name__} as encryption")
    elif not encryption in tuple( ['caesar', 'vigenere', 'hill'] ):
        raise ValueError("encryption need to be one of the following values: " +
                         "'caesar', 'vigenere', or 'hill'")

    elif len(key) != 1 and encryption == 'caesar':
        raise ValueError(f"'{key}' need to have a lenght of 1")

    cipher: str = str()

    for i in range(len(plain)):
        cipher += caesar.encrypt.charSubs(plain[i], key[i % len(key)])

    return cipher

