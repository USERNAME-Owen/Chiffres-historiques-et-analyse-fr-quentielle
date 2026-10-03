#!/usr/bin/env python3

import random
import json



def gen(lenght: int) -> str:
    if not isinstance(lenght, int):
        raise typeError(f"can't use non-int of type '{type(lenght).__name__}' as lenght")
    else if lenght < 0:
        raise valueError("lenght need to be greater or equal than 0")

    table = 

