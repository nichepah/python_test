#!/bin/python

if __name__ == "__main__":
    """ This is the main function.
    
    Prints g(x) = x/(1-x)^2
 
    """
    for i in range(10):
        x = 0.1*i
        print(x, x/(1-x*x))
