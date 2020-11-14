import pytest
from linked_list.linked_list import LinkedList


# Can successfully instantiate an empty linked list
def test_empty_list():
    assert LinkedList()


# Can properly insert into the linked list
def test_insert():
    L = LinkedList()
    L.insert("a")
    L.insert("b")
    assert L.head.value == "b"
    assert L.head.next.value == "a"

 # The head property will properly point to the first node in the linked list


def test_first_node():
    L = LinkedList()
    assert L.head == None

# Can properly insert multiple nodes into the linked list


def test_insert_multiple():
    L = LinkedList()
    L.insert("c")
    L.insert("b")
    L.insert("a")
    actual = str(L)
    print(actual)
    expected = " { a } -> { b } -> { c } -> NULL"
    assert actual == expected

# Will return true when finding a value within the linked list that exists


def test_true_value():
    L = LinkedList()
    L.insert("c")
    L.insert("b")
    L.insert("a")
    actual = L.includes("c")
    expected = True
    assert actual == expected

    # Will return false when searching for a value in the linked list that does not exist


def test_false_value():
    L = LinkedList()
    L.insert("c")
    L.insert("b")
    L.insert("a")
    actual = L.includes("z")
    expected = False
    assert actual == expected

# Can properly return a collection of all the values that exist in the linked list


def test_values():
    L = LinkedList()
    L.insert("c")
    L.insert("b")
    L.insert("a")
    actual = L.value_list()
    print(actual)
    expected = ["a", "b", "c"]
    assert actual == expected
