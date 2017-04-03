from .interface import AbstractLinkedList
from linked_list import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for value in elements:
                self.append(value)

    def __str__(self):
        if len(self) == 0:
            return "[]"
            
        result = []
        for item in self:
            result.append(item.elem)
        return "{}".format(result)

    def __len__(self):
        counter = 0
        for thing in self:
            counter+=1
        return counter

    def __iter__(self):
        current = self.start
        while current:
            yield current
            current = current.next
        raise StopIteration

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError
        if len(self) == 0:
            raise IndexError
        for ticker, value in enumerate(self):
            if ticker == index:
                return value.elem

    def __add__(self, other):
        combined = LinkedList()
        for item in self:
            combined.append(item.elem)
        for item in other:
            combined.append(item.elem)
        return combined

    def __iadd__(self, other):
        for item in other:
            self.append(item.elem)
        return self
        

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for item in zip(self, other):
            if item[0].elem != item[1].elem:
                return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
        

    def append(self, elem):
        current = Node(elem)
        if self.start:
            self.end.next = current
            self.end = current
        else:
            self.start = current
            self.end = self.start

    def count(self):
        return len(self)

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index >= len(self):
            raise IndexError
        if len(self) == 0:
            raise IndexError
        
        previous = None
        current = self.start
        counter = 0
        
        while current:
 
            if index == counter:
                if previous is None:
                    self.start = self.start.next
                    return current.elem
                
                if current.next is None:
                    previous.next = None
                    self.end = previous
                    return current.elem
                
                previous.next = current.next
                return current.elem
                
            counter+=1
            previous = current
            current = current.next
                
            
