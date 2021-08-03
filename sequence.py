def hailstone(n):
    if type(n) != int:
        raise TypeError("'n' must be type int")
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        seq.append(n)
    return seq


def fibonacci(n):
    if type(n) != int:
        raise TypeError("'n' must be type int")
    a, b = 0, 1
    seq = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        seq.append(b)
    return seq


print(fibonacci(50.0))
