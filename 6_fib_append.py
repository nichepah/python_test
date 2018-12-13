def fib_append(n):
    """ Function to implement fibonacci series.

    Get 'n' from keyboard, call fib_append(n), return fibonacci series up to n,
    then print the series"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    x = int(input(" Please enter a number: "))
    print("fib_append(x)")
    print(fib_append(x))