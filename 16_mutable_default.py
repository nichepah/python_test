def mutable_default(a, L=[]):
    """ Defaults args get accumulated in mutable objects like Lists."""
    L.append(a)
    return L


if __name__ == "__main__":
    """ Program to pass a list as a default argument to a function. 
    
    Function should add a value passed in to it to the default List. Observe the counter-intuitive accumulation of 
    variables in the same list
    """
    # mutable default arguments
    print("mutable default, adds 1 to L", mutable_default(1))
    print("mutable default, adds 2 to L", mutable_default(2))
    print("mutable default, adds 3 to L", mutable_default(2))
