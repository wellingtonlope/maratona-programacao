# Máximo Divisor Comum
def mdc(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Número primos
def ehPrimo(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Juros composto
# M = C * (1 + i)t
# M=montante; C=capital; i=taxa; t=tempo
100 * (1 + 0.05) ** 2
