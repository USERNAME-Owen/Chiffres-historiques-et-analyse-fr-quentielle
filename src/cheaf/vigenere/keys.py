#!/usr/bin/env python3

from cheaf import caesar



def genKey(lenght: int) -> str:
    if not isinstance(lenght, int):
        raise TypeError(f"can't use non-int of type '{type(lenght).__name__}' as lenght")
    elif lenght < 0:
        raise ValueError("lenght need to be greater or equal than 0")

    key: str = str()
    
    for i in range(lenght):
        key += caesar.keys.genKey()

    return key

