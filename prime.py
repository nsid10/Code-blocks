def primality(n: int) -> bool:
    """
    Brute force primality test

    Returns True if input is a prime number
    """
    if type(n) != int:
        raise TypeError("input must be type int")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5 + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primality_MR(n: int, k=10, base=[2], randomBase=True) -> bool:
    """
    Generalized Miller–Rabin primality test

    Returns True if input is a prime number

    Args:
        n (int): Number
        k (int, optional): No. of random bases to test against. Ignored if randomBase is False. Defaults to 10.
        base (list, optional): Custom base values. Ignored if randomBase is True. Defaults to [2].
        randomBase (bool, optional): Defaults to True.
    """
    from random import randrange

    if type(n) != int:
        raise TypeError("input must be type int")
    if n < 2:
        return False

    # Trial division test with small primes
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        if n == p:
            return True
        elif n % p == 0:
            return False

    if randomBase:
        base = [randrange(2, n - 2) for _ in range(k)]

    # Miller-Rabin primality test
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in base:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def primality_Baillie_PSW(n: int) -> bool:
    """
    Baillie–PSW primality test

    Trial division > Base 2 Miller-Rabin test > Perfect square test > Strong Lucas prime test

    Returns True if input is a prime number
    """

    def jacobi_symbol(a: int, k: int) -> int:
        """
        Calculates the Jacobi symbol
        """
        a, j = a % k, 1
        while a != 0:
            while a % 2 == 0:
                a //= 2
                if k % 8 in (3, 5):
                    j = -j
            if a % 4 == 3 and k % 4 == 3:
                j = -j
            a, k = k % a, a
        return j if k == 1 else 0

    if type(n) != int:
        raise TypeError("input must be type int")
    if n < 2:
        return False

    # Trial division test with small primes
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        if n == p:
            return True
        elif n % p == 0:
            return False

    # Base 2 Miller-Rabin primality test
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    x = pow(2, d, n)
    if x != 1 and x != n - 1:
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    # Perfect square test using Newton's method
    c = (n.bit_length() - 1) // 2
    a, d = 1, 0
    for s in reversed(range(c.bit_length())):
        e, d = d, c >> s
        a = (a << d - e - 1) + (n >> 2 * c - e - d + 1) // a
    if (a - (a * a > n)) ** 2 == n:
        return False

    # Strong Lucas probable prime test
    d = 5
    while jacobi_symbol(d, n) != -1:
        d += 2 if d > 0 else -2
        d = -d

    k, s = n + 1, 0
    while k % 2 == 0:
        k //= 2
        s += 1

    u, v, q = 1, 1, (1 - d) // 4
    b = k.bit_length()
    while b > 1:
        u = (u * v) % n
        v = (v * v - 2 * q) % n
        q = pow(q, 2, n)
        b -= 1
        if (k >> (b - 1)) & 1:
            u, v = u + v, v + u * d
            u = (u + n) // 2 if u & 1 else u // 2
            v = (v + n) // 2 if v & 1 else v // 2
            q *= (1 - d) // 4

    u, v = u % n, v % n
    if u == 0 or v == 0:
        return True

    for r in range(1, s):
        v = (v * v - 2 * q) % n
        if v == 0:
            return True
        q = pow(q, 2, n)
    return False


def prime_factors(n: int) -> list:
    """
    Prime factorization

    Returns a list of prime factors of input
    """
    if type(n) != int:
        raise TypeError("input must be type int")
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    while n % 3 == 0:
        n //= 3
        factors.append(3)
    i = 5
    limit = int(n ** 0.5)
    while i <= limit:
        if n % i == 0:
            n //= i
            limit = int(n ** 0.5)
            factors.append(i)
        elif n % (i + 2) == 0:
            n //= i + 2
            limit = int(n ** 0.5)
            factors.append(i + 2)
        else:
            i += 6
    if n != 1:
        factors.append(n)
    return factors


def prime_sieve(n: int) -> list:
    """
    Sieve of Eratosthenes

    Returns a list of prime numbers less than input
    """
    if type(n) != int:
        raise TypeError("input must be type int")
    if n < 3:
        return []
    number = [True] * (n // 2)
    for i in range(3, int(n ** 0.5 + 1), 2):
        if number[i // 2]:
            number[i * i // 2 :: i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if number[i]]
