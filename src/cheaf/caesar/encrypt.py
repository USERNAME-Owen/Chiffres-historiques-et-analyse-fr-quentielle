#!/usr/bin/env python3

from cheaf import io
from cheaf import caesar



def charSubs(plain_char: str, key: str) -> str:
    if not isinstance(plain_char, str):
        raise TypeError(f"can't use non-str of type '{type(plain_char).__name__}' as plain_char")
    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type '{type(key).__name__}' as key")

    ascii_table: dict[str:int] = io.table.getTable()
    ascii_values: tuple[str] = tuple(ascii_table.keys())

    cipher_index: int = (ascii_table[plain_char] - 32 + ascii_table[key] - 32) % len(ascii_table)

    return ascii_values[cipher_index]


def plainSubs(plain: str, key: str, type: str) -> str:
    if not isinstance(plain, str):
        raise TypeError(f"can't use non-str of type {type(plain).__name__} as plain")
    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type {type(key).__name__} as key")

    cipher: str = str()

    for i in range(len(plain)):
        cipher += caesar.encrypt.charSubs(plain[i], key[i % len(key)])

    return cipher

