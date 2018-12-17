import json

if __name__ == "__main__":
    """ Converts json to dict
    
    """
    # json string
    my_json = '{"plant":"BSP", "shop":"RailMIll", "product":"Rail"}'
    # convert to dict
    my_dict = json.loads(my_json)
    # print the dict
    print("my_dict", my_dict)

