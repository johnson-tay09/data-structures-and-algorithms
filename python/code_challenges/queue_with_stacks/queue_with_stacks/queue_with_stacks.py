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

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top:
            return False
        return True
        # (return not self.top) most pythonic


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # use stack to add to back of que
    # if empty, push node to collection
    # if not empty, pop node then push node to bank until empty
    # then push node to collection
    # then pop and push bank back to collection
    def enqueue(self, value):

        # empty queue
        if not self.stack1.top:
            self.stack1.push(value)
            return
        # pop
        while self.stack1.top:
            temp = self.stack1.pop()
            # push to bank
            self.stack2.push(temp)
        self.stack2.push(value)
        # push back to stack1 w/ new node @ bottom
        while self.stack2.top:
            temp2 = self.stack2.pop()
            self.stack1.push(temp2)

    # use stack to remove from front of que
    def dequeue(self):
        return self.stack1.pop()
