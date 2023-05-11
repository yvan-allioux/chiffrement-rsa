import pytest
from rsa import *

def test_exponentiation_rapide():
    assert exponentiation_rapide(2, 10, 1000) == 24
    assert exponentiation_rapide(3, 3, 10) == 7
    assert exponentiation_rapide(5, 0, 13) == 1

def test_coefficients_bezout():
    x, y = coefficients_bezout(42, 56)
    assert x * 42 + y * 56 == pgcd(42, 56)

def test_nombre_est_premier():
    assert nombre_est_premier(1) == False
    assert nombre_est_premier(2) == True
    assert nombre_est_premier(4) == False
    assert nombre_est_premier(7) == True

def test_recherche_prochain_nombre_premier():
    assert recherche_prochain_nombre_premier(20) == 23
    assert recherche_prochain_nombre_premier(1) == 2

def test_pgcd():
    assert pgcd(14, 28) == 14
    assert pgcd(21, 14) == 7

def test_recherche_prochain_nombre_premier_avec_phi_n():
    phi_n = 100
    min_var = 346
    assert recherche_prochain_nombre_premier_avec_phi_n(min_var, phi_n) == 347
    assert recherche_prochain_nombre_premier_avec_phi_n(9876, 74) == 9877


def test_text_to_binary():
    assert text_to_binary("A") == "01000001"
    assert text_to_binary("salut comment ça va ?") == "011100110110000101101100011101010111010000100000011000110110111101101101011011010110010101101110011101000010000011100111011000010010000001110110011000010010000000111111"


def test_binary_to_text():
    assert binary_to_text("01000001") == "A"
    assert binary_to_text("011100110110000101101100011101010111010000100000011000110110111101101101011011010110010101101110011101000010000011100111011000010010000001110110011000010010000000111111") == "salut comment ça va ?"

def test_int_to_text():
    assert int_to_text(65) == "A"

def test_text_to_int():
    assert text_to_int("A") == 65

def test_chiffrement_RSA():
    m = 65
    e = 3
    p = 11
    q = 17
    n = p * q
    c = chiffrement_RSA(m, e, n)
    assert c == 109

def test_dechiffrement_RSA():
    m = 65
    e = 3
    p = 11
    q = 17
    n = p * q
    phi_n = (p - 1) * (q - 1)
    c = 109
    d = coefficients_bezout(e, phi_n)[0] % phi_n
    decrypted = dechiffrement_RSA(c, d, n)
    assert decrypted == 65

def test_key_clear():
    assert key_clear("172ffa1f92e5b0ed9a5-229867e7") == (6843715585200947648933, 580413415)
    assert key_clear("172ffa1f92e5b0ed9a5-1607b79a7af94bc7877") == (6843715585200947648933, 6502151240857165789303)

def test_hex():
    var_hex = "172ffa1f92e5b0ed9a5"
    var_int = int(var_hex, 16)
    var_hex_result = hex(var_int)[2:]
    assert var_hex_result == var_hex

def test_chiffrement_dechiffrement():
    test_pub = "172ffa1f92e5b0ed9a5-229867e7"
    test_m = "salut"

    test_m_int = text_to_int(test_m)
    test_n, test_e = key_clear(test_pub)

    test_leng_n = len(str(abs(test_n)))
    test_leng_m = len(str(abs(test_m_int)))
    assert test_leng_m < test_leng_n
    #chiffrement
    test_c = chiffrement_RSA(test_m_int, test_e, test_n)
    test_c_hex = hex(test_c)[2:]

    #test_c_hex peut etre envoyé

    #dechiffrement
    priv = "172ffa1f92e5b0ed9a5-1607b79a7af94bc7877"
    test_c_hex = test_c_hex

    test_n, test_d = key_clear(priv)
    test_c = int(test_c_hex, 16)
    m_result_int = dechiffrement_RSA(test_c, test_d, test_n)
    m_result_text = int_to_text(m_result_int)

    assert m_result_text == test_m

def test_decoupage_int_en_blocs_plus1():
    assert decoupage_int_en_blocs_plus1(123456789, 2) == [112, 134, 156, 178, 19]
    assert decoupage_int_en_blocs_plus1(123456789, 8) == [112345678, 19]
    assert decoupage_int_en_blocs_plus1(123456789, 9) == [1123456789]
    assert decoupage_int_en_blocs_plus1(544467283666114334728142787847140735094807035110519333515912566699781498728398571574480531964225, 21) == [1544467283666114334728, 1142787847140735094807, 1035110519333515912566, 1699781498728398571574, 1480531964225]


def test_chiffrement_dechiffrement_block():
    test_pub = "172ffa1f92e5b0ed9a5-229867e7"
    test_m = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    test_m_int = text_to_int(test_m)
    test_n, test_e = key_clear(test_pub)

    # Découpage en blocs
    leng_n = len(str(abs(test_n)))
    leng_m = len(str(abs(test_m_int)))
    if leng_m >= leng_n:
        blocs = decoupage_int_en_blocs_plus1(test_m_int, leng_n - 2)
    else:
        blocs = [test_m_int]
    print(blocs)
    # Chiffrement
    m = ""
    for bloc in blocs:
        print("chhifre : " + str(chiffrement_RSA(bloc, test_e, test_n)))
        m = m + hex(chiffrement_RSA(bloc, test_e, test_n))[2:] + "-"

    # test_c_hex peut être envoyé

    # Déchiffrement
    priv = "172ffa1f92e5b0ed9a5-1607b79a7af94bc7877"
    test_c_hex = m
    n, d = key_clear(priv)
    c_tab = string_block_clear(test_c_hex)
    # Addition des blocs
    m_result = ""
    for i in range(len(c_tab)):
        bloc = c_tab[i]
        bloc = hex(block_to_int)[2:]
        bloc = dechiffrement_RSA(bloc, d, n)
        bloc = str(bloc)
        bloc = bloc[1:]
        m_result = m_result + bloc
    # Conversion en texte
    m_result_text = int_to_text(int(m_result))

    assert m_result_text == test_m


