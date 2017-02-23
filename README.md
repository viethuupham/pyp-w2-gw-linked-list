# [pyp-w2] Linked list

Today's project consist of building a LinkedList. You can think of it as a re implementation of a regular Python List.

A `LinkedList` (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure and is constructed as a "chain" of Nodes. We'll see in detail how Nodes work because they're the objects holding the LinkedList structure.

### Nodes

Node are simple Python objects that have two values:

* An element (any python object): `1`, `hello`, `[1, 2, 3]`
* And a reference to another Node (that can be None, if the node is not connected to any other Node)

They can be created in the following way:

```python
n1 = Node(12)  # next is None
n2 = Node(99)  # next is None
n3 = Node(37)  # next is None
```

We can create a "chain" of nodes by connecting each one of these nodes to their respective "next" nodes:

```python
n1.next = n2  # 12 -> 99
n2.next = n3  # 99 -> 37
```

Seen graphically, we'd end up with something like the following image:

![linked_list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

### The structure of a LinkedList

A LinkedList will just be an extremely simple object that will rely in Nodes to provide its behavior. A list is just an object that has two values: `start` and `end`. `start` points to the first Node in the list, and `end` points to the last Node in the list. **We don't keep references of the nodes in between.**.

![linkedlist](https://cloud.githubusercontent.com/assets/872296/23283799/c779c290-fa06-11e6-854b-62cbf00bce4f.png)

Following our previous example, our list would look something like:

```python
# n1 -> n2 -> n3
# 12 -> 99 -> 37
my_list = LinkedList(start=n1, end=n3)  # WARNING! Not the actual interface.
                                        # Just for clarity purposes
```

This is all that we need to provide all the behavior of a regular list. If you don't believe me check Hint 1 ;)

### Important considerations for lists

As a regular Python `list`, it must be an ordered collection. Meaning that new Nodes in the list must be appended and iterated respecting certain order.

To create a new linked list, you just have to instantiate the `LinkedList` class, like this:

```python
>>> l = LinkedList()
```

It must also be possible to instantiate a new `LinkedList` using a pre loaded set of elements:

```python
>>> l = LinkedList([1, 5, 10])
```

Appending new elements to the list is possible by calling the `append` method:

```python
>>> l.append("hello")
>>> l.append(10)
>>> l.append("good bye")
```

To get the length of the list at certain time, call the `count` method, or just apply the `len()` built-in function to the list:

```python
>>> l.count()
3
>>> len(l)
3
```

You must also implement support to concatenate other linked lists to the current one. As in Python's `list`, there must be two possible ways of doing that, one mutating the original list:

```python
>>> l = LinkedList([1, 2, 3])
>>> l += LinkedList([8, 9, 10])
>>> len(l)
6
```

And other one not mutating it:

```python
>>> l = LinkedList([1, 2, 3])
>>> new_l = l + LinkedList([8, 9, 10])
>>> len(l)
3
>>> len(new_l)
6
```

The `pop` method must be supported to extract elements from the list.
`pop` without any parameter must return and extract the last element of the list, and `pop(n)` must do the same thing with the `nth` element in it. Example:

```python
>>> l = LinkedList([2, 4, 6, 8, 10])
>>> len(l)
5
>>> l.pop()  # return the last element
10
>>> len(l)
4
>>> l.pop(0)  # return the fist element
2
>>> len(l)
3
```

To see the String representation of a `LinkedList` at any time, you must use the `str` built-in function, or just `print` it:

```python
>>> str(l)
"[2, 4, 6, 8, 10]"
>>> print(l)
"[2, 4, 6, 8, 10]"
```

There's a last, but not less important requirement. Two `LinkedList`s containing the same elements in the same order must be considered equal:

```python
>>> LinkedList([2, 4, 6, 8]) == LinkedList([2, 4, 6, 8])
True
>>> LinkedList([2, 4, 6, 8]) == LinkedList([4, 2, 6, 8])
False
```

## Extra: coverage

Once your LinkedList is ready and your tests are passing, check to see the coverage report. It'll surely be missing a few lines, as we haven't included tests for `__getitem__` and `__ne__`. Write the missing tests to take the coverage above 95%.
