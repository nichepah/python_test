def fib(n):
    """ Function to implement fibonacci series.

    Get 'n' from keyboard, call fib(n) to print fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print(b)
        # pay attention to multiple variable assignment
        a, b = b, a+b