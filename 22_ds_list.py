if __name__ == "__main__":
    """ List as a data structure.
    
    Demo of more functions and attributes of list
    """
    my_list = [ 1, 2, 3, 2,"Ammu", 2,"Julie"]
    my_list.append("mappa")
    print(my_list)
    b = [8, 9, 10]
    my_list.extend(b)
    print(my_list)
    my_list.insert(3, "Masha")
    # removes first occurance of the item; error if it doesnt exist
    my_list.remove(9)
    # pops last item; If index given, pops that item; returns the popped item
    k = my_list.pop()
    print(my_list)
    # returns the position of the item
    print(my_list.index(3))
    # returns number of times the item is found
    print(my_list.count(2))
    # sorts items, in place
    string_list = ['k', 't', 'd', 'c']
    string_list.sort()
    print(string_list)
    # reverse items in place
    string_list.reverse()
    print(string_list)



