if __name__ == "__main__":
    """ Demo sets.

    Unordered collection, no duplicate allowed; create using set() function
    good for membership testing and eliminating duplicates
    union, intersection, difference, and symmetric difference.
    """
    students = set(('masha', 'shopkins', 'maya', 'bear', 'tasha', 'shopkins'))
    # duplicates removed
    # run in several times, observe the order of items
    print(students)
    # check membership
    print('masha' in students)
    # add an item
    students.add("Ishita")
    print(students)
    # update with more than 1 item
    students.update(['samyukta', 'harsh', 'lopamudra'])
    print(students)
    # other functions
    print(len(students))
    # pop doesnt make much sense, but works
    # print(students.pop())
    # remove
    students.remove('bear')
    # delete the set itself
    del students
    # error try printing the set
    # print(students)
    # set operations
    word_1 = set('nincompoop')
    print(word_1)
    word_2 = set('panacea')
    print(word_2)
    print("word_1 - word_2", word_1 - word_2)
    print("word_1 | word_2", word_1 | word_2)
    print("word_1 & word_2", word_1 & word_2)
    print("word_1 ^ word_2", word_1 ^ word_2)

