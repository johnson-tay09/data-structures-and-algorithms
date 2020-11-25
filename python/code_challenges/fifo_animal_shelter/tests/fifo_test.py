import pytest


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


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

    # def peek(self):
    #     if not self.front:
    #         raise InvalidOperationError("Method not allowed on empty collection")
    #     return self.front.value

    def is_empty(self):
        # return boolean true as self.front is falsys
        return not self.front

    def dequeue(self):
        # if not self.front:
        #     raise InvalidOperationError("Method not allowed on empty collection")
        # save front node into a variable
        target_node = self.front
        # reassign front node to to old front.next
        self.front = target_node.next
        # return stored node
        return target_node.value


class AnimalShelter:
    # initiate class with a queue for each cats and dogs
    def __init__(self):
        self.dog_q = Queue()
        self.cat_q = Queue()

    # add dogs to dog queue and cats to cat queue or return null

    def enqueue(self, value):
        if value.lower() == "dog":
            self.dog_q.enqueue(value)
            return
        elif value.lower() == "cat":
            self.cat_q.enqueue(value)
            return
        return "Null"

    # return preferred animal
    def dequeue(self, preference):
        if preference.lower() == "dog":
            return self.dog_q.dequeue()
        elif preference.lower() == "cat":
            return self.cat_q.dequeue()
        return "Null"


def test_enqueue():
    q = AnimalShelter()
    q.enqueue("dog")
    actual = q.dog_q.front.value
    expected = "dog"
    assert actual == expected


def test_dequeue():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("dog")
    actual = q.dequeue("cat")
    expected = "cat"
    assert actual == expected
