if __name__ == "__main__":
    """ Demo dict.
    
    un-orderd set of key value pair, created with dict() or {}
    Indexed by keys, not numbers as in lists
    """
    roll_no = {'masha': 12, 'shopkins': 23, 'maya': 2}
    # unordered
    print(roll_no)
    # key as index
    print(roll_no['masha'])
    # list keys
    print(list(roll_no.keys()))
    # sorted list of keys
    print(sorted(list(roll_no.keys())))
    # membership as in set
    print("'masha' in roll_no", 'masha' in roll_no)
    print("'bear' in roll_no", 'bear' in roll_no)
    # dict comprehension
    cube = {x: x**3 for x in range(20)}
    print(cube)
    mobile_no = dict(aneesh=8986880000, natasha=8986880432, angela=89868804300)
    print(mobile_no)
    print("looping")
    for i, v in enumerate(roll_no):
        print(i, v)

