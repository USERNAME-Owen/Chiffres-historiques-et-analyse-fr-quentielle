#!/usr/bin/env python 3

import random

from cheaf import io



def genKey() -> str:
    ascii_table: dict[str:int] = io.table.read(io.table.getPath())
    ascii_values: tuple[str] = tuple(ascii_table.keys())

    return random.choice(values_list)

