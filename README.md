# vigenere_cipher
EPITA-X : SAE Développer un outil ou un jeu - Sujet A - Algorithme de chiffrement Vigenère

Installation et lancement

Prérequis
- Python 3 installé
- Système Linux / MacOS ou terminal compatible bash installé

```
chmod +x application.sh
./application.sh
```
OU
```
python3 chiffrement_vigenere_finale.py
```

1. Introduction

Ce projet a pour objectif principal d’implémenter en Python l’algorithme de chiffrement de Vigenère, puis d’y ajouter plusieurs fonctionnalités complémentaires afin d’illustrer différents aspects de la sécurité de l’information.

Le projet ne se limite pas au simple chiffrement et déchiffrement d’un message. Il intègre également une analyse statistique par l’entropie de Shannon ainsi qu’une fonctionnalité de stéganographie par image bitmap.

L’objectif est pédagogique : comprendre comment protéger le contenu d’un message par chiffrement, comment mesurer sa complexité statistique et comment dissimuler l’existence même de ce message dans un support visuel.

2. Fonctionnalités développées

2.1 Chiffrement et déchiffrement de Vigenère

L’algorithme de Vigenère est un chiffrement polyalphabétique basé sur une clé répétée. Chaque caractère du message est décalé selon la lettre correspondante de la clé.

Dans l’implémentation Python, le message est parcouru caractère par caractère. La clé est répétée pour correspondre à la longueur du message. Chaque lettre est convertie en une valeur numérique comprise entre 0 et 25, puis un décalage est appliqué à l’aide d’un calcul modulo 26.

Le chiffrement et le déchiffrement sont réalisés dans deux fonctions distinctes, ce qui permet une utilisation claire et modulaire dans le programme principal.

2.2 Génération et modification de clé

Le programme permet de créer une clé de chiffrement de deux manières :

-	génération aléatoire d’une clé de longueur choisie

-	saisie manuelle d’une clé personnelle

Cette fonctionnalité permet à l’utilisateur de contrôler la complexité de son chiffrement.

2.3 Calcul de l’entropie de Shannon

L’entropie de Shannon est utilisée pour mesurer le niveau de désordre ou d’imprévisibilité d’un message.

Dans l’implémentation, la fréquence d’apparition de chaque caractère est calculée, puis transformée en probabilité. La formule de Shannon est ensuite appliquée afin d’obtenir un score numérique.

Cette fonctionnalité permet de comparer un message clair et un message chiffré et de montrer que le chiffrement augmente l’entropie, ce qui signifie que le texte devient statistiquement plus aléatoire.

2.4 Stéganographie par image bitmap (LSB)

La stéganographie est une technique qui consiste à cacher un message dans un support afin de masquer son existence.

Dans ce projet, le message chiffré est dissimulé dans une image bitmap (BMP) à l’aide de la méthode LSB (Least Significant Bit).

Le format BMP a été choisi car il stocke les pixels sans compression. Chaque pixel est représenté par trois octets correspondant aux composantes bleu, vert et rouge.

Le principe consiste à modifier le bit de poids faible de chaque octet pixel pour y insérer un bit du message chiffré. Cette modification change la valeur de l’octet de ±1 maximum, ce qui est visuellement imperceptible.

2.5 Sauvegarde et menu interactif

Le programme permet également :

-	d’enregistrer un message chiffré ou déchiffré dans un fichier texte

-	de naviguer dans un menu interactif en ligne de commande

-	de lancer l’application via un script application.sh

3 Auteurs

Équipe E16 – EPITA-X

Bachelor Cybersécurité – CYB1

4 Licence 

Projet pédagogique – EPITA-X

Utilisation libre dans un cadre éducatif.
