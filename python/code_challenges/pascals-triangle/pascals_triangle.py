def binomialCoefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def printPascal(n):
    # Iterate through every line
    # and print entries in it
    if n < 1:
        return "Not a valid input"
    for line in range(0, n):
        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print(binomialCoefficient(line, i), " ", end="")
        print()


printPascal(2)
