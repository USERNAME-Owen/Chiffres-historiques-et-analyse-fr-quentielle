#!/usr/bin/env python3

from cheaf import io
from cheaf import caesar



def charSub(text_char: str, key: str) -> str:
    if not isinstance(text_char, str):
        raise TypeError(f"can't use non-str of type '{type(text_char).__name__}' as path")
    elif not isinstance(key, str):
        raise TypeError(f"can't use non-str of type '{type(key).__name__}' as path")

    ascii_table = io.table.read(io.table.getPath())

    encrypted_char = (ascii_table[text_char] - 32 + ascii_table[key] - 32) % len(ascii_table)
    values_list = tuple(ascii_table.keys())

    return values_list[encrypted_char]

