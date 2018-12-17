if __name__ == "__main__":
    """ Some trivial info
    
    1. Use str() and eval() to convert between string and int
    2. formatted printing # harsh
    3. __name__ to access the module name
    """
    # 1
    print(1 + eval('2'))
    print(str(1 + eval('2')))
    # 2
    print("The factors of 35 are %d and %d" % (7, 5))
    # use it as a variable
    x = "The factors of 35 are %d and %d" % (7, 5)
    print("x: ", x)
    # on import it will print module name
    print(__name__)



