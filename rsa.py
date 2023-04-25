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
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def recherche_prochain_nombre_premier(min):
    i = min
    while (nombre_est_premier(i) != True):
        i += 1
    return i

def chiffrement_RSA(m, e, n):
    return exponentiation_rapide(m, e, n)

# Exemple d'utilisation
if __name__ == "__main__":
    # Exponentiation rapide (calculer les grandes puissances d'un nombre entier modulo un autre nombre entier)
    print("Exponentiation rapide: ", exponentiation_rapide(2, 10, 1000))  # 1024 % 1000 = 24

    # Coefficients de Bezout
    a, b = 42, 56
    x, y = coefficients_bezout(a, b)
    print("Coefficients de Bezout: ", x, y)  # x * 42 + y * 56 = pgcd(42, 56)



    # Chiffrement RSA
    m = 65  # Message à chiffrer (ASCII de 'A')
    e = 3  # Exposant public : e entre 1 et phi(n) et premier avec phi(n) (taille de 16 à 32 bits c'est mieux)
    n = 187  # Modulo (p * q, où p et q sont des nombres premiers)
    c = chiffrement_RSA(m, e, n)
    print("Message chiffré: ", c)

    grandRandom = random.randint(1000000000, 10000000000) # entre 10 chiffres et 11 chiffres
    print(grandRandom)
    print(recherche_prochain_nombre_premier(grandRandom))
