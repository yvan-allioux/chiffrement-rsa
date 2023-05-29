import math
import random

"""
Calcule l'exponentiation rapide, ce qui est utile pour les grands nombres en cryptographie.
Paramètres: base (int), exposant (int), modulo (int)
"""
def exponentiation_rapide(base, exposant, modulo):
    if modulo == 1:
        return 0
    resultat = 1
    base = base % modulo
    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * base) % modulo
        exposant = exposant // 2
        base = (base * base) % modulo
    return resultat

"""
Calcule les coefficients de Bézout de deux nombres, qui sont utilisés dans l'algorithme
d'Euclide étendu pour trouver le plus grand commun diviseur (PGCD).
Paramètres: a (int), b (int)
"""
def coefficients_bezout(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0

"""
Vérifie si un nombre est premier, ce qui est important pour la génération de clés dans RSA.
Paramètres: n (int)
"""
def nombre_est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
Recherche le prochain nombre premier à partir d'un nombre minimum donné.
Paramètres: min (int)
"""
def recherche_prochain_nombre_premier(min):
    i = min
    while (nombre_est_premier(i) != True):
        i += 1
    return i

"""
Calcule le plus grand commun diviseur de deux nombres.
Paramètres: a (int), b (int)
"""
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

"""
Recherche le prochain nombre premier qui est coprime avec phi_n.
Paramètres: min (int), phi_n (int)
"""
def recherche_prochain_nombre_premier_avec_phi_n(min, phi_n_param):
    i = min
    while (pgcd(phi_n_param, i) != 1):
        i += 1
    return i

"""
Convertissent le texte en représentation binaire.
Paramètres: text (str)
"""
def text_to_binary(text):
    binary_representation = ""
    for char in text:
        binary_char = bin(ord(char))[2:]  # Retirer le préfixe "0b"
        binary_representation += binary_char.zfill(8)  # Remplir avec des zéros à gauche pour obtenir 8 bits
    return binary_representation

"""
Convertissent une valeur binaire sous forme de texte en texte.
Paramètres: binary_string (str)
"""
def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):  # Parcourir la chaîne binaire par groupes de 8 bits
        binary_char = binary_string[i:i + 8]
        char = chr(int(binary_char, 2))  # Convertir le groupe de bits en un caractère
        text += char
    return text

"""
Convertissent une valeur entière en texte en utilisant la représentation binaire.
Paramètres: integer_value (int)
"""
def int_to_text(integer_value):
    binary_string = bin(integer_value)[2:]
    # Ajouter des zéros à gauche si nécessaire pour obtenir un multiple de 8 bits
    binary_string = binary_string.zfill((len(binary_string) + 7) // 8 * 8)
    text = binary_to_text(binary_string)
    return text

"""
conversion entre texte et entier.
Paramètres: text (str)
"""
def text_to_int(text):
    binary_string = text_to_binary(text)
    integer_value = int(binary_string, 2)
    return integer_value

"""
conversion entre texte et entier.
Paramètres: integer (int)
"""
def int_to_text2(integer):
    binary_string = format(integer, '08b')
    text = ''.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    return text

"""
conversion entre texte et entier
Paramètres: text (str)
"""
def text_to_int2(text):
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    integer_value = int(binary_string, 2)
    return integer_value

"""
ette fonction prend une clé RSA sous forme de chaîne hexadécimale
et la divise en ses deux composantes entières.
Paramètres: key (str)
"""
def key_clear(key):
    n_hex = key.split('-')[0]
    n = int(n_hex, 16)
    e_or_d_hex = key.partition('-')[2]
    e_or_d = int(e_or_d_hex, 16)
    return n, e_or_d

"""
Convertit une chaîne hexadécimale en une liste de blocs hexadécimaux.
Paramètres: stringHex (str)
"""
def stringHex_to_tabHex(stringHex):
    blocks_list = stringHex.split('-')
    blocks_list.pop()
    return blocks_list

"""
Découpe un nombre entier en blocs de taille spécifiée.
Paramètres: intVar (int), taille (int)
"""
def decoupage_int_en_blocs_plus1(intVar, taille):
    strVar = str(intVar)
    blocs = [strVar[i:i + taille] for i in range(0, len(strVar), taille)]
    return [int('1' + bloc) for bloc in blocs]

"""
Convertit une liste de blocs hexadécimaux en une liste de nombres entiers.
Paramètres: blocs (str)
"""
def tabHex_to_tabInt(blocs):
    m_result = []
    for bloc in blocs:
        bloc_int = int(bloc, 16)
        m_result.append(bloc_int)
    return m_result

"""
échiffre une liste de blocs chiffrés à l'aide d'une clé privée RSA.
Paramètres: m (str), d (int), n (int)
"""
def dechiffrement_tableau(m, d, n):
    m_result = []
    for bloc in m:
        m_result.append(dechiffrement_RSA(bloc, d, n))
    return m_result

"""
Retire le premier caractère de chaque élément dans la liste s'il s'agit d'un "1".
Paramètres: arr (str)
"""
def remove_first_char_if_one(arr):
    result = []
    for num in arr:
        num_str = str(num)
        if num_str.startswith("1"):
            num_str = num_str[1:]
        result.append(int(num_str))
    return result

"""
Convertit une liste de chaînes de caractères en une seule chaîne de caractères.
Paramètres: arr (str)
"""
def tabStr_to_str(arr):
    result = ""
    for s in arr:
        result += str(s)
    return result

"""
effectuent le chiffrement sur un bloc de message.
Paramètres: m (int), e (int), n (int)
"""
def chiffrement_RSA(m, e, n):
    return exponentiation_rapide(m, e, n)

"""
effectuent le déchiffrement RSA sur un bloc de message.
Paramètres: m (int), d (int), n (int)
"""
def dechiffrement_RSA(m, d, n):
    return exponentiation_rapide(m, d, n)

"""
Cette fonction effectue le chiffrement RSA sur un message texte à l'aide d'une clé publique RSA.
Paramètres: cle_pub (str), text (str)
"""
def chiffrement_RSA_text(cle_pub, text):
    test_n, test_e = key_clear(cle_pub)
    #Conversion en int du message
    test_m_int = text_to_int2(text)
    #Découpage en blocs du message int et ajou de 1
    leng_n = len(str(abs(test_n)))
    leng_m = len(str(abs(test_m_int)))
    if leng_m >= leng_n:
        blocs = decoupage_int_en_blocs_plus1(test_m_int, leng_n - 2)
    else:
        blocs = [test_m_int]
    #Chiffrement de chaque block int plus 1
    #Conversion en Hex des block chiffré
    #Addition des block hex séparé par des -
    m = ""
    for bloc in blocs:
        m = m + hex(chiffrement_RSA(bloc, test_e, test_n))[2:] + "-"
    return m

"""
Cette fonction effectue le déchiffrement RSA sur un message chiffré à l'aide d'une clé privée RSA.
Paramètres: cle_prive (str), text (str)
"""
def dechiffrement_RSA_text(cle_prive, text):
    n, d = key_clear(cle_prive)
    #string block hex séparé par des - converti en tableau dex
    m_hex_tab = stringHex_to_tabHex(text)
    #Tableau de blocs hex en tableau de int
    m_int_tab = tabHex_to_tabInt(m_hex_tab)
    #Dechiffrement des block int
    m_dechiff_tabInt = dechiffrement_tableau(m_int_tab, d, n)
    #Découpage des int en enlevant les "1" devant les chiffres, renvois un tableau de String
    m_dechiff_tabStr_moin1 = remove_first_char_if_one(m_dechiff_tabInt)
    #Conversion tableau de string en grand String
    m_result_str = tabStr_to_str(m_dechiff_tabStr_moin1)
    #Conversion String ver int
    m_result_int = int(m_result_str)
    #Conversion int ver message
    m_result_text = int_to_text2(m_result_int)
    return m_result_text


if __name__ == "__main__":
    # Exponentiation rapide (calculer les grandes puissances d'un nombre entier modulo un autre nombre entier)
    #print("Exponentiation rapide: ", exponentiation_rapide(2, 10, 1000))  # 1024 % 1000 = 24

    # Coefficients de Bezout
    #a, b = 42, 56
    #x, y = coefficients_bezout(a, b)
    #print("Coefficients de Bezout: ", x, y)  # x * 42 + y * 56 = pgcd(42, 56)


    print("MENU RSA ENCRYPTION")
    print("1 Encrypt")
    print("2 Decrypt")
    print("3 New Key generation")
    print("4 Exit\n")

    mode = input()

    if mode == "1":
        print("----Encrypt----")
        print("Clé publique :")
        key_user_input_hex = input()
        print("Message en claire :")
        text_user_input_clear = input()
        print("Message chiffré :")
        
        print(chiffrement_RSA_text(key_user_input_hex, text_user_input_clear))

    elif mode == "2":
        print("----Decrypt----")
        print("Clé privée :")
        key_user_input_hex = input()
        print("Message chiffré :")
        text_user_input_hex = input()
        print("Message déchiffré :")

        print(dechiffrement_RSA_text(key_user_input_hex, text_user_input_hex))

    elif mode == "3":
        p = recherche_prochain_nombre_premier(random.randint(10000000000, 1000000000000))
        q = recherche_prochain_nombre_premier(random.randint(10000000000, 1000000000000))
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = recherche_prochain_nombre_premier_avec_phi_n(random.randint(10000000, 1000000000), phi_n)
        d = coefficients_bezout(e, phi_n)[0] % phi_n
        if (e >= phi_n):
            print("erreur e >= phi_n")
        if (pgcd(e, phi_n) != 1):
            print("erreur pgcd(e, phi_n) != 1")
        if (d >= phi_n):
            print("erreur d >= phi_n")
        e_hex = hex(e)[2:]
        n_hex = hex(n)[2:]
        print("cle publique (n leng " + str(len(str(abs(n)))) + "): " + n_hex + "-" + e_hex)
        d_hex = hex(d)[2:]
        print("cle privee: " + n_hex + "-" + d_hex)
    elif mode == "4":
        print("----Exit----")
    else:
        print("Error")

    

