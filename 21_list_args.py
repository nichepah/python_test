if __name__ == "__main__":
    """ Program to print an arithmetic series. 
     
     Get the start of the series, end, and the common difference from the user.
     Hint: use input()
     use map(function that acts on data, data)
     then pass on *list to range
     """
    user_input = list(map(int, input("Enter start, end, and commod_diff \n").strip().split(',')))
    # print(user_input)
    my_ap = list(range(*user_input))
    for i in my_ap:
        print(i)


