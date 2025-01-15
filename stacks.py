from typing import Any


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def __len__(self):
        return len(self.__items)

    def is_empty(self):
        return self.__len__() == 0

    def pop(self) -> Any:
        return self.__items.pop() if not self.is_empty() else f'Stack is empty!'

    def peek(self):
        return self.__items[-1]

    def size(self):
        counter = 0
        for _ in self.__items:
            counter += 1
        return counter

    def reverse(self):
        return self.__items[::-1]

    def __repr__(self):
        if self.is_empty():
            return 'Empty Stack Found!.'
        return f'{self.__items}'
