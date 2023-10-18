# Cryptomath Module
# https://www.nostarch.com/crackingcodes (BSD Licensed)


def gcd(a, b) -> int:
    """
    Function for finding the greatest common denominator of two provided integers
    :param a: First value to compare
    :type a: int
    :param b: Second value to compare
    :type b: int
    :return: int
    """
    while a != 0: # Keep going until we reach the lowest we can go
        a, b = b % a, a # Euclid's formula for calculating GCD
    return b # once a == 0 return b as the GCD


def findModInverse(a, m) -> int | None:
    """
    Function for finding the modulo inverse of two provided integers
    :param a: Integer to calculate
    :type a: int
    :param m: Modulo to calculate
    :type m: int
    :return: int
    """
    if gcd(a, m) != 1:
        return None # There is no modulo inverse if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0: # Continue calculating until the formula attempts to calculate for modulo of 0
        q = u3 // v3 # Perform integer division on the values(basically "non-decimal, rounded down division")
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3 # Looks like a massive, entangled version of Euclid's formula for GCD
    return u1 % m
