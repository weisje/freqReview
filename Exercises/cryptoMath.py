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


# TODO
def findModInverse(a, m) -> int:
    """
    Function for finding the modulo inverse of two provided integers
    :param a: First value to calculate
    :type a: int
    :param m: Second value to calculate
    :type m: int
    :return: int
    """
    pass