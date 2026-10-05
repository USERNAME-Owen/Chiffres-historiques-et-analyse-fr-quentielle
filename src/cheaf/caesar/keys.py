#!/usr/bin/env python 3

import random

from cheaf import io



def genChar() -> str:
    ascii_table: dict[str:str] = io.table.read(io.table.getPath())
    
    values_list = tuple(ascii_table.values())
    return random.choice(values_list)


def genKey(lenght: int) -> str:
    if not isinstance(lenght, int):
        raise typeError(f"can't use non-int of type '{type(lenght).__name__}' as lenght")
    elif lenght < 0:
        raise valueError("lenght need to be greater or equal than 0")

    key = str()

    for i in range(lenght):
        key += genChar()

    return key

