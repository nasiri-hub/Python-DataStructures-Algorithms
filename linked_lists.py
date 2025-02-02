
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_last(self, item: int):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def add_first(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def index_of(self, item: int):
        current = self.head
        index: int = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, item: int):
        if self.index_of(item) != -1:
            return True
        return False

    def remove_first(self):
        if self.is_empty():
            raise IndexError('List is empty.')

        elif self.head.next is None:
            self.head = None
        else:
            second = self.head.next
            self.head = second

    def remove_last(self):
        if self.is_empty():
            raise IndexError('List is empty.')
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next and current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def get_size(self):
        current = self.head
        counter = 0
        while current:
            current = current.next
            counter += 1
        return counter

    def to_array(self):
        array: list[int] = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    def print(self, convert=False):
        if convert:
            print(f'{self.to_array()}')
            return
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next

    # **Reversing the Linked lists
    def reverse(self):
        if self.is_empty():
            raise IndexError('List is empty.')
        previous = None
        current = self.head
        while current:
            last = current.next
            current.next = previous
            previous = current
            current = last

        self.head = previous


def main():
    ll = LinkedList()
    ll.add_first(10)
    ll.add_last(20)
    ll.add_last(30)
    ll.add_last(40)

    ll.reverse()
    ll.print(convert=True)


if __name__ == '__main__':
    main()
