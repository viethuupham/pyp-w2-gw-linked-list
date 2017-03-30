# Hint 2 - Appending

Adding nodes to our list is going to be extremely simple. We just need to place the new node in the correct position of our "node chain".

## Appending
Let's understand first how we'd "append a node" to an already created list of nodes:

```python
n1 = Node(12)
n2 = Node(99)
n3 = Node(37)

n1.next = n2  # 12 -> 99
n2.next = n3  # 99 -> 37

start = n1
end = n3

# We kill the n* references to simulate our list
del n1
del n2
del n3

# Our Node chain up to this point:
# Node(12) > Node(99) > Node(37)
#  ^start                ^end

# Let's append the number 18
# We first create the node:
n4 = Node(18)

# and we connect them to the list of nodes:
end.next = n4

# Now our node chain looks something like:
# Node(12) > Node(99) > Node(37) > Node(18)
#  ^start                ^end

# We have to obviously move the `end` node to point to the new node
end = n4

# Finally, our chain looks like:
# Node(12) > Node(99) > Node(37) > Node(18)
#  ^start                           ^end
```

This is how the append method would look like:

```python
class LinkedList(object):
    # ... your code ...

    def append(self, elem):
      new_node = Node(elem)
      if self.start is None:
          self.start = new_node
          self.end = self.start
      else:
          self.end.next = new_node
          self.end = new_node
```

In this particular case we have to make sure our list is not initially empty. If that's the case, we need to also point `start` to the recently created node.

## Bonus: Creating the list

The `__init__` method accepts an optional list to pre-populate the created list. Example:

```python
l = LinkedList([3, 2, 1])
```

Once your `append` method is ready, you can rely on it for your initialization method:

```python
class LinkedList(object):
    def __init__(self, elements=None):
        self.start = None
        self.start = None
        if elements:
            for elem in elements:
                self.append(elem)
```
