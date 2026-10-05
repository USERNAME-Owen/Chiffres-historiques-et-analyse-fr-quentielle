#!/usr/bin/env python 3

import random

from cheaf import io



def genChar() -> str:
    ascii_table: dict[str:str] = io.table.read(io.table.getPath())
    
    values_list = tuple(ascii_table.values())
    return random.choice(values_list)

