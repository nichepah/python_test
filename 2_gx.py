#!/bin/python
""" Prints g(x) = x/(1-x)^2, for values i%2==1 """

#range function uses list
def g(x):
    for i in range(10):
        x = 0.1*i
        print x/(1-x*x)

for i in range(10):
    if i%2 == 1:
        print i
        print g(0.1*i)
