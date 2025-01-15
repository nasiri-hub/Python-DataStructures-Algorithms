# Python Data Structures & Algorithms (DSA)

***DSA is about finding efficient way to store and retrieve data, to perform operations on data, and to solve specific problems.***

It's a fundamental part of computer science «CS» , that teaches us how to think and solve complex problems systematically, using right **DSA** makes your program run faster.

### Data Structures :
- **Data Structures** are used to organize information in various ways, and how data can be stored in different structures. So that it can be efficiently operated on by algorithms.

- We structure data in different ways, depending on what we have what we wanna do with it.

- They give us the possibility to manage large amount of data, efficiently for uses such as a large databases and internet indexing services.

- They are essential ingredients in creating fast and powerful algorithms, they help in managing and organizing data, reduce complexity and increase efficiently.

#### Data Structures Types :
In **CS** there are two different kinds of data structures :

- **1 - Primitive Data Structures :**
  - They are basic data structures provided by programming languages, to represent single values such as « Strings, Numbers, Boolean ».

- **2- Abstract Data Structures :**
	- They are higher-level data structures that are built using primitive data types, and provide more complex and specialized options.
	 **.e.g :** «List, Array, Dictionary, Linked List, Stack, Queue, Trees and Graphs»


### Algorithms :
Is about how to solve difference problems, often by searching through and manipulating data-structures.
An algorithms is a set of step-by-step instructions to solve a given problem or achieved a specific goal.
**.E.G :** 
- Finding what user search for " Search Engine ".
- Sorting.

#### Algorithm Characteristics :
- **Algorithm complexity** :
  - Space complexity :
	  - How much memory does it require?
  - Time complexity :
	  - How much time does it take to complete?
- **Inputs and output** :
  - What does the algorithm accept , and what are the results?
- **Classification** :
  - Serial/parallel, exact/approximate, deterministic/non-deterministic

### Space Complexity :
A measure of the amount of memory an algorithm uses, depending on the amount of data the algorithm is working on.
When we talk about space complexity , we only look at the additional space that we should allocate relative to the size of the input we have always the input of size (n), so we don't count it we just analyze how much space we need to allocate for this algorithm.

### Time Complexity :
A measure of the amount of time an algorithm takes to run, depending on the amount of data that algorithm working on.

### Divide and Conquer :
 A method of solving complex problems, by breaking them into smaller, more manageable sub-problems,  the sub-problems, and combining the solutions.
 «Recursion» is often used when using this method in an algorithm.

### Brute Force :
A simple and straight forward way an algorithm, can work by simply trying all possible solutions and them choosing the best one.


# - Linked Lists in Python

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
