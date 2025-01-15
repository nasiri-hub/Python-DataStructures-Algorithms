from collections import deque


class Queue:
    def __init__(self):
        self.__items = deque([])

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        return self.__items.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        return self.__items[0]

    def is_empty(self):
        return self.__len__() == 0

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f'{self.__items}'
