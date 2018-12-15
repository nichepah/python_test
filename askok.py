defVal = 10


def my_func(arg=defVal):
    print(arg)


def ask_ok(prompt, retries=3, message="Please enter 'yes' or 'no' "):
    """Prompt handler.

    specify the prompt as a string.
    retries, message have defaults (3, and a string)
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yep'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries-1
        if retries == 0:
            print("Too many wrong attempts")
            return
        print(message)


def mutable_default(a, L=[]):
    """ Defaults args get accumulated in mutable objects like Lists.

    """
    L.append(a)
    return L


def mutable_default_2(a, L=None):
    """ Defaults with mutable objects, in a predictable way.

    """
    if L is None:
        L=[]
    L.append(a)
    return L


if __name__ == "__main__":
    my_func()
    my_func(20)
    print("with only default values")
    ask_ok("Please enter yes or no: ")
    print("retries=2")
    ask_ok("Please enter yes or no: ", retries=2)
    print("message changed")
    ask_ok(" Please enter y or n")
    # mutable default arguments
    print("mutable default, adds 1 to L", mutable_default(1))
    print("mutable default, adds 2 to L", mutable_default(2))
    print("mutable default, adds 3 to L", mutable_default(2))
    # mutable exclusively for each call
    print("mutable default, adds 1 to L", mutable_default_2(1))
    print("mutable default, adds 2 to L", mutable_default_2(2))
    print("mutable default, adds 2 to L", mutable_default_2(2))

