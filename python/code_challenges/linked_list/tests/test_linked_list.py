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

# .append(value) which adds a new node with the given value to the end of the list


def test_append():
    L = LinkedList()
    L.append_list("a")
    L.append_list("b")
    L.append_list("c")
    actual = L.value_list()
    print(actual)
    expected = ["a", "b", "c"]
    assert actual == expected
# .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node


def test_insert_before():
    L = LinkedList()
    L.append_list("a")
    L.append_list("b")
    L.append_list("c")
    L.insert_before("c", "z")
    actual = L.value_list()
    print(actual)
    expected = ["a", "b", "z", "c"]
    assert actual == expected
    L.insert_before("a", "y")
    actual = L.value_list()
    print(actual)
    expected = ["y", "a", "b", "z", "c"]
    assert actual == expected

# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node


def test_insert_after():
    L = LinkedList()
    L.append_list("a")
    L.append_list("b")
    L.append_list("c")
    L.insert_after("b", "z")
    actual = L.value_list()
    print(actual)
    expected = ["a", "b", "z", "c"]
    assert actual == expected
    L.insert_after("c", "y")
    actual = L.value_list()
    print(actual)
    expected = ["a", "b", "z", "c", "y"]
    assert actual == expected

# Can successfully add a node to the end of the linked list
# Can successfully add multiple nodes to the end of a linked list
# Can successfully insert a node before a node located i the middle of a linked list
# Can successfully insert a node before the first node of a linked list
# Can successfully insert after a node in the middle of the linked list
# Can successfully insert a node after the last node of the linked list
