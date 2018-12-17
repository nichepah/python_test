import json

if __name__ == "__main__":
    """ Converts dict to json 

    """
    # json string
    my_dict = {'product': 'Rail', 'shop': 'RailMIll', 'plant': 'BSP'}
    # convert to dict
    my_json = json.dumps(my_dict)
    # print the dict
    print("my_json", my_json)
