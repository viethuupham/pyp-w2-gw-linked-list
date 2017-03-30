# Hint 3 - The power of iteration

Many of the LinkedList methods can be quickly implemented by relying on the iterator of the list. For example, the count method could be easily implemented like:

```python
class LinkedList(object):
    # ... your code ...

    def count(self):
      counter = 0
      for _ in self:
        counter += 1
      return counter
```

A good base to implement the iterator pattern into the LinkedList might be:

```python
class LinkedListIterable(object):
    # ... your code ...
    def __next__(self):
        pass

    __next__ = next


class LinkedList(object):
    # ... your code ...
    def __iter__(self):
        return LinkedListIterable(self.start)
```
