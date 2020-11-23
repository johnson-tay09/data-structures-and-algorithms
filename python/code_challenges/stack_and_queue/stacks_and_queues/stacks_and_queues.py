class InvalidOperationError(Exception):
    pass


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        # new node on top of stack gets next value of previous top stack node
        node.next = self.top
        # new node becomes top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top:
            return False
        return True
        # (return not self.top) most pythonic

    def peek(self):
        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        return self.top.value


class Queue:

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, value):
        node = Node(value)
        # is the list empty?
        if not self.front:
            self.front = node
            self.back = node
            return
        # current back next value becomes new node
        self.back.next = node
        # the new back is the new node
        self.back = node

    def peek(self):
        if not self.front:
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        # return boolean true as self.front is falsy
        return not self.front

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        # save front node into a variable
        target_node = self.front
        # reassign front node to to old front.next
        self.front = target_node.next
        # return stored node
        return target_node.value
