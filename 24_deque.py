# import collections.deque
from collections import deque

# my_queue = collections.deque([1, 2, 3, 4, 5])
if __name__ == "__main__":
    my_deque = deque([1, 2, 3, 4, 5])
    my_deque.append(6)
    my_deque.appendleft(7)
    print(my_deque)
    print(my_deque.pop())
    print(my_deque.popleft())
