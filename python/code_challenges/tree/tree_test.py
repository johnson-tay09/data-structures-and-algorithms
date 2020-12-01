import pytest
from .tree import BinaryTree, BinarySearchTree, Node

# # Can successfully instantiate an empty tree


# def test_init_empty():
#     t = BinaryTree()
#     actual = t.value
#     expected = None
#     assert actual == expected
# # Can successfully instantiate a tree with a single root node


# def test_single():
#     t = BinaryTree()
#     a = Node(3)
#     t.root = a
#     actual = t.root.value
#     expected = 3
#     assert actual == expected

#     # Can successfully add a left child and right child to a single root node


# def test_add():
#     t = BinaryTree()
#     a = Node(3)
#     b = Node(2)
#     c = Node(5)
#     t.root = a
#     a.left = b
#     a.right = c
#     actual = a.left.value + a.right.value
#     expected = 7
#     assert actual == expected

#     # Can successfully return a collection from a preorder traversal


# def test_preorder():
#     t = BinaryTree()
#     a = Node(3)
#     b = Node(2)
#     c = Node(5)
#     t.root = a
#     a.left = b
#     a.right = c
#     t.pre_order()
#     # Can successfully return a collection from an inorder traversal


# def test_inorder():
#     t = BinaryTree()
#     a = Node(3)
#     b = Node(2)
#     c = Node(5)
#     t.root = a
#     a.left = b
#     a.right = c
#     t.in_order()
#     # Can successfully return a collection from a postorder traversal


# def test_postorder():
#     t = BinaryTree()
#     a = Node(3)
#     b = Node(2)
#     c = Node(5)
#     t.root = a
#     a.left = b
#     a.right = c
#     t.post_order()

# # text find max function


def test_find_empty():
    t = BinaryTree()
    actual = t.find_max_value()
    expected = None
    assert actual == expected


def test_find_max():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    t.root = a
    a.left = b
    a.right = c
    actual = t.find_max_value()
    expected = 5
    assert actual == expected


def test_multi_max():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    d = Node(5)
    t.root = a
    a.left = b
    a.right = c
    b.left = d
    actual = t.find_max_value()
    expected = 5
    assert actual == expected
# 0, 1 2 and many


def test_many_max():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    d = Node(5)
    g = Node(8)
    h = Node(22)
    i = Node(1)
    j = Node(19)
    k = Node(56)
    t.root = a
    a.left = b
    a.right = c
    b.left = d
    d.right = g
    d.left = h
    h.left = i
    i.right = j
    j.left = k
    actual = t.find_max_value()
    expected = 56
    assert actual == expected
