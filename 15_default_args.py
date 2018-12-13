def ask_ok(prompt, retries=3, message="Please enter 'yes' or 'no' "):
    """ Demo keyword arguments.

    This function implements a demo case for default arguments.
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yep'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries-1
        if retries == 0:
            print("Too many wrong attempts", message)
            return


if __name__ == "__main__":
    """ Program to check if the user input is Yes or No. 
    
    Accept as yes, even if the user enters yes/y/yep. Similarly for No/n/nope. On any other response, attempt to get 
    input from the user 'i' times. i should be an argument to the function with default value of 3. After finishing i 
    number of wrong attempts, print a message to the user "Please enter only yes or no" 
    """
    print("with only default values")
    k = ask_ok("Please enter yes or no: ")
    print("k", k)
    print("retries=2")
    k = ask_ok("Please enter yes or no: ", retries=2)
    print("k", k)
    print("message changed")
    k = ask_ok("Please enter y or n")
    print("k", k)
    # show function.__ stuff
    print(ask_ok.__name__)
    print(__name__)
