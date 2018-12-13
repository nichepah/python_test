if __name__ == "__main__":
    """Program to insert "bear" to the beginning of a list if it contains "masha".
     
     """
    my_string_list = ['jerry', 'bear', 'mickey', 'tom']
    # create a copy of the mutable and then operate on it; First try without [:]
    for x in my_string_list[:]:
        if x == "bear":
            my_string_list.insert(0, "masha")

    for x in my_string_list:
        print(x)

