import sys
fib = __import__('5_fib')
fib_append = __import__('6_fib_append')


if __name__ == "__main__":
    """" Import fib and fib_append from 5_fib.py and 6_fib_append.py
    
    dir() shows definitions in the module
    """
    print(fib.fib(10))
    print(fib_append.fib_append(100))
    print(dir(fib))
    print(dir(sys))

