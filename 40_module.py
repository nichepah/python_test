import sys
# imports askok.py
# try without if __name__ == "__main__" in askok.py
import askok
import sail.rbu.mti.whoami
# import sail.rbu.mti.whoami as mt
# from sail.rbu.rdcis import whoami


# since the file name starts with a numeral
fib = __import__('5_fib')
fib_append = __import__('6_fib_append')


if __name__ == "__main__":
    """" Import fib and fib_append from 5_fib.py and 6_fib_append.py
    
    dir() shows definitions in the module
    try other functions and attributes
    imports askok.py
    imports from sail.rbu.mti.whoami.py a function whoami
    """
    print(fib.fib(10))
    print(fib_append.fib_append(100))
    print(dir(fib))
    print(dir(sys))
    askok.ask_ok("is it ok(y/s)")
    sail.rbu.mti.whoami.whoami()
    # mt.whoami()
    # whoami.whoami()




