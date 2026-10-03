#!/usr/bin/env python3

import os



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

