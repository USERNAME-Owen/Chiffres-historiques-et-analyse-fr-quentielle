"""
================================================================================
        PROGRAMME DE CHIFFREMENT/DÉCHIFFREMENT - CHIFFRE DE VIGENÈRE
================================================================================

Description:
    Programme interactif permettant de chiffrer et déchiffrer des messages
    en utilisant l'algorithme de Vigenère avec une clé personnalisée ou
    aléatoire.

Fonctionnalités:
    - Chiffrement de messages (fichier ou saisie manuelle)
    - Déchiffrement de messages (fichier ou saisie manuelle)
    - Génération de clés aléatoires ou personnalisées
    - Enregistrement des messages dans des fichiers
    - Calcul de l'entropie pour évaluer la sécurité du chiffrement
    - Visualisation en temps réel de la clé, du dernier message chiffré et dechiffré
    - Interface en ligne de commande interactive

Auteur: GONDRY Alexi, DE LAGAYE DE LANTEUIL JEAN, TOPOLOV Vladimyr, VIGANT Eliot
Date: Janvier 2026
Version: 2.9

================================================================================
"""

import math
import random
import struct


# ================================================================================
#                           FONCTION DE CHIFFREMENT
# ================================================================================
def chiffrage(message_a_chiffrer, ma_cle):
    """
    Chiffre un message en utilisant l'algorithme de Vigenère.

    Principe:
        Pour chaque lettre du message, on applique un décalage dans l'alphabet
        correspondant à la lettre de la clé à la position correspondante.

    Args:
        message_a_chiffrer (str): Le message en clair à chiffrer
        ma_cle (str): La clé de chiffrement (uniquement des lettres)

    Returns:
        str: Le message chiffré en majuscules

    Exemple:
        >>> chiffrage("HELLO", "KEY")
        'RIJVS'
    """
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    message_chiffrer = ""
    a = 0
    for i in message_a_chiffrer.upper():
        if i in alphabet_list:
            alpha_temp = alphabet_list.copy()
            indice = ord(i) - 65
            while alpha_temp[0] != ma_cle[a]:
                alpha_temp.append(alpha_temp.pop(0))
            if a == len(ma_cle) - 1:
                a = 0
            else:
                a += 1
            message_chiffrer += alpha_temp[indice]
        else:
            message_chiffrer += i
    return message_chiffrer


# ================================================================================
#                          FONCTION DE DÉCHIFFREMENT
# ================================================================================
def dechiffrage(message_a_dechiffrer, ma_cle):
    """
    Déchiffre un message chiffré avec l'algorithme de Vigenère.

    Principe:
        Opération inverse du chiffrement. Pour chaque lettre chiffrée, on
        retrouve la lettre originale en utilisant la clé.

    Args:
        message_a_dechiffrer (str): Le message chiffré
        ma_cle (str): La clé de déchiffrement (doit être identique à celle
                      utilisée pour le chiffrement)

    Returns:
        str: Le message déchiffré en majuscules

    Exemple:
        >>> dechiffrage("RIJVS", "KEY")
        'HELLO'
    """
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    message_dechiffrer = ""
    a = 0
    for i in message_a_dechiffrer.upper():
        if i in alphabet_list:
            alpha_temp = alphabet_list.copy()
            while alpha_temp[0] != ma_cle[a]:
                alpha_temp.append(alpha_temp.pop(0))
            if a == len(ma_cle) - 1:
                a = 0
            else:
                a += 1
            for j in alpha_temp:
                if j == i:
                    indice = alpha_temp.index(j)
                    message_dechiffrer += alphabet_list[indice]
                    break
                else:
                    continue
        else:
            message_dechiffrer += i

    return message_dechiffrer


# ================================================================================
#                      FONCTION DE CRÉATION/SAISIE DE CLÉ
# ================================================================================
def obtenir_cle(choix2):
    """
    Permet de générer une clé aléatoire ou d'en saisir une personnalisée.

    Args:
        choix2 (str): '1' pour générer une clé aléatoire
                      '2' pour saisir une clé manuelle

    Returns:
        str: La clé en majuscules, ou None en cas d'erreur

    Validation:
        - Pour une clé manuelle: uniquement des lettres alphabétiques
        - Pour une clé aléatoire: longueur définie par l'utilisateur
    """
    alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if choix2 == '1':
        while True:
            try:
                longueur = int(input("Entrez la longueur de la clé : "))
                if longueur > 0:
                    # On génère et on retourne immédiatement
                    resultat = ''.join(random.choices(alphabet_list, k=longueur))
                    print(f"votre cle est : {resultat}")
                    return resultat.upper()
                else:
                    print("ENTREZ UNE VALEUR SUPERIEUR A 0")
            except ValueError:
                print("Erreur : Entrez un nombre entier.")

    elif choix2 == '2':
        while True:
            resultat = input("Entrer la clé : ")
            if resultat.isalpha():
                print(f"votre cle est : {resultat}")
                return resultat.upper()
            else:
                print("Erreur : La clé ne doit contenir que des lettres (pas d'espaces ni chiffres).")

    return None


# ================================================================================
#                        FONCTION DE CALCUL D'ENTROPIE
# ================================================================================
def entropie(message_chiffrer):
    """
    Calcule l'entropie de Shannon d'un message chiffré.

    L'entropie mesure le degré de désordre/aléatoire du message. Plus
    l'entropie est élevée, plus le message est difficile à décrypter sans
    la clé.

    Args:
        message_chiffrer (str): Le message chiffré à analyser

    Returns:
        float: La valeur d'entropie (entre 0 et ~4.7 pour l'alphabet)
               0 = très prévisible (faible sécurité)
               >4.2 = très aléatoire (forte sécurité)

    Formule:
        H(X) = -Σ p(xi) * log2(p(xi))
        où p(xi) est la probabilité d'apparition de chaque caractère
    """
    occurence = {}
    entropie1 = 0
    counter = 0
    for i in message_chiffrer:
        if i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]:
            counter += 1
            if i in occurence:
                occurence[i] += 1
            else:
                occurence[i] = 1
    for i in occurence:
        occurence[i] /= counter
    for i in occurence:
        entropie1 += occurence[i] * math.log(occurence[i], 2)
    return -entropie1

# ================================================================================
#                            FONCTION DE STEGANOGRAPHIE/CACHER
# ================================================================================

def cacher_message_bmp(image_in, image_out, message):
    """
    cache un message texte dans une image BMP avec la methode LSB
    image_in  : image BMP source
    image_out : image BMP de sortie
    message   : message a cacher (texte)
    """

    # lire l image en binaire
    data = bytearray(open(image_in, "rb").read())

    # lire l offset des pixels (octets 10 a 13 du BMP)
    offset = struct.unpack("<I", data[10:14])[0]

    # transformer message bytes + marqueur
    message_bytes = message.encode("utf-8") + b"###"

    bit_index = 0

    for byte in message_bytes:
        # parcourir chaque bit de l octet (de 7 a 0)
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1

            # modif lsb
            data[offset + bit_index] = (data[offset + bit_index] & 0b11111110) | bit

            bit_index += 1

    # save img.bmp
    open(image_out, "wb").write(data)

# ================================================================================
#                            FONCTION DE STEGANOGRAPHIE/EXTRAIRE
# ================================================================================

def extraire_message_bmp(image):
    """
    extrait un message cache dans une image BMP avec la methode LSB
    image : image BMP contenant un message
    """

    # lire img binaire
    try:
        data = open(image, "rb").read()

    # lire offset pixel
        offset = struct.unpack("<I", data[10:14])[0]

    # recup tous les lsb
        bits = [b & 1 for b in data[offset:]]

        message = bytearray()

    # grouper par 8 pour octets
        for i in range(0, len(bits), 8):
            byte = 0
            for bit in bits[i:i + 8]:
                byte = (byte << 1) | bit

            message.append(byte)

        # break si marqueur
            if message.endswith(b"###"):
                break

    # remove marqueur
        return message[:-3].decode("utf-8")

    except Exception as e:
        return e

# ================================================================================
#                            PROGRAMME PRINCIPAL
# ================================================================================

# Variables globales pour stocker l'état du programme
ma_cle = "SECURITE"  # Clé de chiffrement par défaut
message_chiffrer = None  # Stocke le dernier message chiffré
message_dechiffrer = None  # Stocke le dernier message déchiffré

# Boucle principale du menu
while True:
    choix = input("------------------------------------------------------------"
                  "\nBIENVENUE DANS VOTRE PROGRAMME DE CHIFFREMENT. VEUILLEZ SELECTIONNER UNE OPTION : "
                  "\n1 : chiffrer "
                  "\n2 : dechiffrer "
                  "\n3 : cree/modifier la cle"
                  "\n4 : enregister"
                  "\n5 : entropy"
                  "\n6 : steganographie"
                  "\n7 : visualiser"
                  "\n8 : quitter"
                  "\nCHOIX : ")

    # ================================================================================
    #                         OPTION 1 : CHIFFREMENT
    # ================================================================================
    if choix == '1':
        if ma_cle is not None:
            choix2 = input(
                "------------------------------------------------------------\nTRES BIEN. VOULEZ VOUS CHIFFRER A PARTIR D'UN FICHIER : "
                "\n1 : oui"
                "\n2 : non"
                "\nCHOIX : ")
            while True:
                if choix2 == '1':
                    fichier = input("ENTREZ LE NOM DU FICHIER : ")
                    try:
                        with open(f"{fichier}.txt", "r") as fichier:
                            message_a_chiffrer = fichier.read()
                        break
                    except FileNotFoundError:
                        print("Le fichier n'existe pas")

                elif choix2 == '2':
                    message_a_chiffrer = input("ENTREZ LE MESSAGE A CHIFFRER : ")
                    break
                else:
                    choix2 = input("ENTRE UNE REPONSE VALIDE (1 ou 2) : ")

            # Appel de la fonction de chiffrement
            message_chiffrer = chiffrage(message_a_chiffrer, ma_cle)

            # Affichage du résultat
            print(f"------------------------------------------------------------"
                  f"\nVotre message chiffrer est : {message_chiffrer}\nVotre cle est : {ma_cle}")
            false = False

        else:
            print("------------------------------------------------------------"
                  "\nVOUS N'AVEZ PAS DE CLE ENREGISTRE. VEUILLEZ EN ENREGISTER UNE AVANT.")

    # ================================================================================
    #                        OPTION 2 : DÉCHIFFREMENT
    # ================================================================================
    elif choix == '2':
        if ma_cle is not None:
            choix2 = input("TRES BIEN. VOULEZ VOUS DECHIFFRER A PARTIR D'UN FICHIER : "
                           "\n1 : oui"
                           "\n2 : non"
                           "\nCHOIX : ")
            while True:
                if choix2 == '1':
                    fichier = input("ENTREZ LE NOM DU FICHIER : ")
                    try:
                        with open(f"{fichier}.txt", "r") as fichier:
                            message_a_dechiffrer = fichier.read()
                        message_dechiffrer = dechiffrage(message_a_dechiffrer, ma_cle)
                        print(f"Votre message dechiffrer est : {message_dechiffrer}\nVotre cle est : {ma_cle}")
                        break
                    except FileNotFoundError:
                        print("Le fichier n'existe pas")

                elif choix2 == '2':
                    message_a_dechiffrer = input("ENTREZ LE MESSAGE A DECHIFFRER : ")
                    message_dechiffrer = dechiffrage(message_a_dechiffrer, ma_cle)
                    print(f"Votre message dechiffrer est : {message_dechiffrer}\nVotre cle est : {ma_cle}")
                    break

                else:
                    choix2 = input("ENTREZ UNE REPONSE VALIDE (1 ou 2) : ")

        else:
            print("------------------------------------------------------------"
                  "\nVOUS N'AVEZ PAS DE CLE ENREGISTRE. VEUILLEZ EN ENREGISTER UNE AVANT.")

    # ================================================================================
    #                    OPTION 3 : CRÉATION/MODIFICATION DE CLÉ
    # ================================================================================
    elif choix == '3':
        choix2 = input("1 : cle aleatoire"
                       "\n2 : cle perso"
                       "\nCHOIX : ")
        while True:
            if choix2 == '1' or choix2 == '2':
                ma_cle = obtenir_cle(choix2)
                break
            else:
                choix2 = input("ENTREZ UNE REPONSE VALIDE (1 ou 2) : ")

    # ================================================================================
    #                    OPTION 4 : ENREGISTREMENT DANS UN FICHIER
    # ================================================================================
    elif choix == '4':
        nom_fichier = input("ENTREZ LE NOM DU FICHIER : ")
        choix2 = input("VOULEZ VOUS ENREGISTER VOTRE MESSAGE CHIFFRE OU DECHIFFRE : "
                       "\n1 : chiffre"
                       "\n2 : dechiffre"
                       "\nCHOIX : ")
        while True:
            if choix2 == '1' and message_chiffrer is not None:
                with open(f"{nom_fichier}.txt", "a") as fichier:
                    fichier.write(f"{message_chiffrer}\n")
                    print("Enregistrement effectue !")
                    break
            elif choix2 == '2' and message_dechiffrer is not None:
                with open(f"{nom_fichier}.txt", "a") as fichier:
                    fichier.write(f"\n{message_dechiffrer}\n")
                    print("Enregistrement effectue !")
                    break
            elif choix2 not in ['1', '2']:
                choix2 = input("ENTREZ UNE REPONSE VALIDE (1 ou 2) : ")
            else:
                print("------------------------------------------------------------"
                      "\nVOUS N'AVEZ NI DE MESSAGE CHIFFRER NI DE MESSAGE DECHIFFRER")
                break

    # ================================================================================
    #                    OPTION 5 : ANALYSE DE L'ENTROPIE
    # ================================================================================
    elif choix == '5':
        if message_chiffrer:
            mon_entropy = entropie(message_chiffrer)
            if 4.7 >= mon_entropy >= 0:
                if 3 >= mon_entropy:
                    print(f"Votre score d'entropy est : {mon_entropy}."
                          f"\nVotre chiffrage est faible, essayer de complexifier votre cle")
                if 4.2 >= mon_entropy > 3:
                    print(f"Votre score d'entropy est : {mon_entropy}."
                          f"\nVotre chiffrage est dans la moyenne, vous pouvez mieux faire")
                if mon_entropy > 4.2:
                    print(f"Votre score d'entropy est : {mon_entropy}."
                          f"\nVotre chiffrage est fort, votre message est dur a dechiffrer")
        else:
            print("------------------------------------------------------------"
                  "\nVOUS N'AVEZ AUCUN MESSAGE A ANALYSER")

    # ================================================================================
    #                         OPTION 6 : STEGANOGRAPHIE
    # ================================================================================

    elif choix == '6':
        choix2 = input("Voulez vous cacher ou extraire :"
                       "\n1 : cacher"
                       "\n2 : extraire"
                       "\nCHOIX : ")
        while True:
            if choix2 == '1':
                if message_chiffrer is not None:
                    image = input("Entrez le nom de l'image : ")
                    image += ".bmp"
                    sortie = input("Entrez le nom du fichier sortant : ")
                    sortie += ".bmp"
                    cacher_message_bmp(image, sortie, message_chiffrer)
                    print("Enregistrement effectue !")
                    break
                else:
                    print("Vous n'avez aucun message a cacher !")
                    break

            elif choix2 == '2':
                fichier = input("Entrez le nom de l'image : ")
                fichier += ".bmp"
                print(extraire_message_bmp(fichier))
                break
            else:
                choix2 = input("ENTREZ UNE REPONSE VALIDE (1 ou 2) : ")
    # ================================================================================
    #                            OPTION 7 : VISUALISER
    # ================================================================================
    elif choix == '7':
        print(f"Votre dernier message chiffré est : {message_chiffrer}"
              f"\nVotre dernier message dechiffrer est : {message_dechiffrer}"
              f"\nvotre dernière clé est : {ma_cle}")

    # ================================================================================
    #                            OPTION 8 : QUITTER
    # ================================================================================

    elif choix == '8':
        print("AU REVOIR !!")
        break

    # ================================================================================
    #                          GESTION DES ERREURS DE SAISIE
    # ================================================================================
    else:
        print("------------------------------------------------------------"
              "\nENTREZ UNE REPONSE VALIDE (1 ou 2 ou 3 ou 4 ou 5 ou 6 ou 7 ou 8)")

# ================================================================================
#                              FIN DU PROGRAMME

# ================================================================================
