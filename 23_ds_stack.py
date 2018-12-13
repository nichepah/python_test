def push(self, val):
    """ Implements push for stack

    :param self:
    :param val:
    :return:
    """
    self.append(val)


if __name__ == "__main__":
    """ List as a stack.

    Implement push and pop
    """
    my_stack = [45, 4, 10, 33, 21, 32, 50]
    print("pop item from list")
    k = my_stack.pop()
    print(k)
    k = my_stack.pop()
    print(k)
    my_stack.pop()
    print(my_stack)
    my_stack.append(70)
    print(my_stack)
