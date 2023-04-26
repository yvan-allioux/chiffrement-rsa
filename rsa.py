import math
import random

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

def coefficients_bezout(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0

def nombre_est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def recherche_prochain_nombre_premier(min):
    i = min
    while (nombre_est_premier(i) != True):
        i += 1
    return i

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def recherche_prochain_nombre_premier_avec_phi_n(min, phi_n_param):
    i = min
    while (pgcd(phi_n_param, i) != 1):
        i += 1
    return i




def text_to_binary(text):
    binary_representation = ""
    for char in text:
        binary_char = bin(ord(char))[2:]  # Retirer le préfixe "0b"
        binary_representation += binary_char.zfill(8)  # Remplir avec des zéros à gauche pour obtenir 8 bits
    return binary_representation

def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):  # Parcourir la chaîne binaire par groupes de 8 bits
        binary_char = binary_string[i:i + 8]
        char = chr(int(binary_char, 2))  # Convertir le groupe de bits en un caractère
        text += char
    return text

def int_to_text(integer_value):
    binary_string = bin(integer_value)[2:]
    # Ajouter des zéros à gauche si nécessaire pour obtenir un multiple de 8 bits
    binary_string = binary_string.zfill((len(binary_string) + 7) // 8 * 8)
    text = binary_to_text(binary_string)
    return text

def text_to_int(text):
    binary_string = text_to_binary(text)
    integer_value = int(binary_string, 2)
    return integer_value

def key_clear(key):
    n_hex = key.split('-')[0]
    n = int(n_hex, 16)
    e_or_d_hex = key.partition('-')[2]
    e_or_d = int(e_or_d_hex, 16)
    return n, e_or_d

def decoupage_int_en_blocs(intVar, taille):
    strVar = str(intVar)
    return [int(strVar[i:i + taille]) for i in range(0, len(strVar), taille)]

def chiffrement_RSA(m, e, n):
    return exponentiation_rapide(m, e, n)

def dechiffrement_RSA(m, d, n):
    return exponentiation_rapide(m, d, n)

# Exemple d'utilisation
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

        int_message = text_to_int(text_user_input_clear)
        n, e = key_clear(key_user_input_hex)
        m = chiffrement_RSA(int_message, e, n)
        m_hex = hex(m)[2:]
        print(m_hex)

    elif mode == "2":
        print("----Decrypt----")
        print("Clé privée :")
        key_user_input_hex = input()
        print("Message chiffré :")
        text_user_input_hex = input()
        print("Message déchiffré :")

        n, d = key_clear(key_user_input_hex)
        c = int(text_user_input_hex, 16)
        m = dechiffrement_RSA(c, d, n)
        m_text = int_to_text(m)
        print(m_text)

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

    

