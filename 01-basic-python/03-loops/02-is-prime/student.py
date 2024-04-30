def is_prime(n):
    prime = False
    if n >= 2:
        prime = True
    for x in range(2, n-1):
        if n%x == 0:
            prime = False
    return prime
