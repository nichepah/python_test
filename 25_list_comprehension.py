if __name__ == "__main__":
    """ Demo List comprehension.
    
    Create a list of cubes of numbers from 1 to 100
    Uses a for loop for definition
    """
    cubes = [x**3 for x in range(1, 100)]
    print(cubes)