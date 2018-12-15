import math

if __name__ == "__main__":
    """ Demo math module.

    """
    x = 1
    y = -2
    # returns y with the sign of x
    k = math.copysign(y, x)
    print(k)
    print(math.fabs(y), math.ceil(3.1), math.floor(8.9), math.trunc(2.45331), math.pow(4, 6), math.exp(10))
    # check the module yourself
    # support for complex numbers, math not necessary
    a = 4.5 + 3j
    print(a, abs(a))





