#!/bin/bash

if [ ! -f "chiffrement_vigenere_finale.py" ]; then
    echo "erreur : fichier introuvable"
    exit 1
fi
python3 chiffrement_vigenere_finale.py
