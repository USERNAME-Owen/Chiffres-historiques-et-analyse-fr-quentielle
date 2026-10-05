#!/usr/bin/env python3

from cheaf import io
from cheaf import caesar



def charSubs(plain_char: str, key: str) -> str:
    if not isinstance(plain_char, str):
        raise TypeError(f"can't use non-str of type '{type(plain_char).__name__}' as path")
    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type '{type(key).__name__}' as path")

    ascii_table: dict[str:int] = io.table.read(io.table.getPath())
    ascii_values: tuple[str] = tuple(ascii_table.keys())

    cipher_index: int = (ascii_table[plain_char] - 32 + ascii_table[key] - 32) % len(ascii_table)

    return ascii_values[cipher_index]


def plainSubs(plain: str, key: str) -> str:
    cipher: str = str()

    for char in plain:
        cipher += charSubs(char, key)

    return cipher

