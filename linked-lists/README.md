# Linked Lists in Python

We use **Linked list** to store a list of objects in sequence, it can grow and shrink automatically.

A Linked List is a linear data structure where each element (node) contains two parts:

- 1. Data: The actual data stored in the node.
- 2. Pointer (or Reference): A reference (pointer) to the next node in the list. also 


## Nodes in Linked Lists
In both the **Singly Linked List** and the **Doubly Linked List**, the list is made up of nodes. A node is a container that holds two or more pieces of information:

- **Data:** The value or data stored in the node.

- **Pointers:** In a **Singly Linked List**, there’s only one pointer (`next`) that points to the next node. In a **Doubly Linked List**, there are two pointers: `next` (pointing to the next node) and `prev` (pointing to the previous node).


## Types of Linked Lists :

- **Singly Linked List:** A linked list where each node contains a reference to the next node.

- **Doubly Linked List:** A linked list where each node contains references to both the next and previous nodes.

- **Circular :**
Both **singly** and **doubly** linked lists can be **circular**, which means the last node will reference the first node.


## Arrays vs Linked Lists

#### 1.Space
- Static arrays have a fixed size, and they may end up with wasting memory.
- Linked lists don't waste memory , but having set that it take a bit of extra memory, because each node should store the address of next node in addition to a value.
- Linked lists are flexible in size because they can dynamically allocate memory as needed.

#### 2.Performance (RunTime Complexity) 
```Python
               (Arrays) - (Linked Lists)
**Lookup**
    - By Index   O(1)        O(n)
    - By Value   O(n)        O(n)

**Insert**
- Beginning/End  O(n)        O(1)
    - Middle     O(n)        O(n)

**Delete**
- Beginning      O(n)        O(1)
    - Middle     O(n)        O(n)
        - End    O(n)        O(1)
``` 

## Getting Started 
```python
def main():
    l = LinkedList()
    l.add_first(10)
    l.add_last(20)
    l.remove_first()
    l.remove_last()
    l.print(convert=True)
    print(l.get_size())
    print(l.to_array())
    print(l.reverse())
    print(l.get_kth_from_the_end(0))

if __name__ == '__main__':
    main()
```
