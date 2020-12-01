import pytest
from tree import BinaryTree, BinarySearchTree, Node

# Can successfully instantiate an empty tree


def test_init_empty():
    t = BinaryTree()
    actual = t.value
    expected = None
    assert actual == expected
# Can successfully instantiate a tree with a single root node


def test_single():
    t = BinaryTree()
    a = Node(3)
    t.root = a
    actual = t.root.value
    expected = 3
    assert actual == expected

    # Can successfully add a left child and right child to a single root node


def test_add():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    t.root = a
    a.left = b
    a.right = c
    actual = a.left.value + a.right.value
    expected = 7
    assert actual == expected

    # Can successfully return a collection from a preorder traversal


def test_preorder():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    t.root = a
    a.left = b
    a.right = c
    t.pre_order()
    # Can successfully return a collection from an inorder traversal


def test_inorder():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    t.root = a
    a.left = b
    a.right = c
    t.in_order()
    # Can successfully return a collection from a postorder traversal


def test_postorder():
    t = BinaryTree()
    a = Node(3)
    b = Node(2)
    c = Node(5)
    t.root = a
    a.left = b
    a.right = c
    t.post_order()
