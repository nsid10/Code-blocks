def fibonacci(n: int) -> list:
    """
    Generates sequence of fibonacci numbers
    """
    if type(n) != int:
        raise TypeError("input must be type int")
    elif n <= 0:
        raise ValueError("input must be greater than zero")

    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-2] + seq[-1])
    return seq


def hailstone(n: int) -> list:
    """
    Generates sequence of hailstone numbers
    """
    if type(n) != int:
        raise TypeError("input must be type int")

    seq = []
    while n not in seq:
        seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return seq
