def isFloatingPrime(f):
    value = 0
    if f[1] != '.':
        return False
    value = int(f[0])
    i = 2
    while i < 5 and i < len(f):
        value *= 10
        value += int(f[i])
        if isPrime(value):
            return True
        i += 1
    return False


def isPrime(n):
    if n > 1:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
    return True


if __name__ == "__main__":
    while True:
        n = input()
        if n is "0.0":
            break
        print("TRUE" if isFloatingPrime(n) else "FALSE")
