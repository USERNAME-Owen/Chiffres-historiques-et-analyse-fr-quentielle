#!/usr/bin/env python3

from cheaf import caesar



def plainSubs(plain: str, key: str) -> str:
    return caesar.encrypt.plainSubs(plain, key, "vigenere")

