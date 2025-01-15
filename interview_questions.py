from stacks import Stack
from queues import Queue
from linked_lists import LinkedList


# *1. Get the Kth from the end
def get_kth_from_the_end(ll: LinkedList, k: int):
    if (ll.is_empty()) or (k <= 0):
        raise ValueError('Invalid value')
    first = ll.head
    second = ll.head
    for _ in range(1, k):
        if second.next is None:
            raise ValueError('Invalid value')
        second = second.next
    while second.next is not None:
        first = first.next
        second = second.next

    return first.data


### *1. Balanced Expressions: ###
class Expression:
    def __init__(self, user_input: str):
        self.stack = Stack()
        self.user_input = user_input
        self.left_brackets = ('(', '{', '[', '<')
        self.right_brackets = (')', '}', ']', '>')

    def is_balanced(self) -> bool:
        for i in self.user_input:
            if i in self.left_brackets:
                self.stack.push(i)
            elif i in self.right_brackets:
                if self.stack.is_empty():
                    return False
                top = self.stack.pop()
                if not self._brackets_match(top, i):
                    return False
        return self.stack.is_empty()

    def _brackets_match(self, left, right):
        return self.left_brackets.index(left) == self.right_brackets.index(right)


### *2. Reversing Queue: ###
def reverse_queue(queue: Queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())

    return queue


### *3. Building a Queue Using Stacks: ###
class QueueByStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):  # O(1)
        self.stack1.push(item)

    def move_stack1_to_stack2(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

    def dequeue(self):  # O(n)
        self.move_stack1_to_stack2()
        return self.stack2.pop()

    def peek(self):  # O(n)
        self.move_stack1_to_stack2()
        return self.stack2.peek()

    def empty(self):
        return len(self.stack1) and len(self.stack2) == 0

    def __repr__(self):
        return f'{self.stack2}'


### *4. Finding Character in String : ###
class CharFinder:
    def __init__(self, input: str):
        self.input = input
        self.ch_frequency_dict: dict = dict()
        self.ch_frequency_set: set = set()

    ## Ex.1: First Non-repeated Character ##
    def find_first_non_repeating_char(self):
        for char in self.input:
            if char in self.ch_frequency_dict:
                self.ch_frequency_dict[char] += 1
            else:
                self.ch_frequency_dict[char] = 1
        for ch in self.ch_frequency_dict:
            if self.ch_frequency_dict.get(ch) == 1:
                return ch

    ## Ex.2: First repeated Character ##
    def find_first_repeated_char(self):
        for char in self.input:
            if char in self.ch_frequency_set:
                return char

            self.ch_frequency_set.add(char)


def main():
    # ch = CharFinder('A Green Apple')
    # print(ch.find_first_non_repeating_char())
    # print(ch.find_first_repeated_char())

    # exp = Expression('<p>(2*5)-[10]</p>')
    # print(exp.is_balanced())

    ll = LinkedList()
    ll.add_first(10)
    ll.add_last(20)
    ll.add_last(30)
    ll.add_last(50)
    print(get_kth_from_the_end(ll, 3))



if __name__ == "__main__":

    main()
