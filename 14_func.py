defVal = 10


def my_func(arg=defVal):
    print(arg)


if __name__ == "__main__":
    """ Functions and default args demo.
    
    Write a function to print value passed to it
    Augment it with a default value
    """
    my_func(20)
    my_func()
