#!/bin/python
""" Prints g(x) = x/(1-x)^2 """

#range function uses list
for i in range(10):
    x = 0.1*i
    print x, x/(1-x*x)

