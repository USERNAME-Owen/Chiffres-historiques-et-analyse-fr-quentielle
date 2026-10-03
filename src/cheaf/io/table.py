#!/usr/bin/env python3

import os
import json



def getRoot() -> str:
    dir: str = os.path.realpath(__file__)

    while os.path.basename(dir) != "cheaf":
        dir = os.path.dirname(dir)

    return dir


def getPath() -> str:
    return os.path.join(
            getRoot(),
            "data",
            "ascii_table.json",
    )


def read(path: str) -> any:
    if not isinstance(path, str):
        raise TypeError(f"can't use non-str of type '{type(lenght).__name__}' as path")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"file '{path}' not found")

    with open(path) as file:
        return json.load(file)

