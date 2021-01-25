from tree_intersection import BinarySearchTree, Node


def test_intersections():
    t = BinarySearchTree()

    t.add(150)
    t.add(100)
    t.add(250)
    t.add(75)
    t.add(160)
    t.add(125)
    t.add(200)
    t.add(350)
    t.add(300)
    t.add(500)
    t.add(400)

    t2 = BinarySearchTree()

    t2.add(42)
    t2.add(100)
    t2.add(600)
    t2.add(200)
    t2.add(350)
    t2.add(4)
    t2.add(500)
    t2.add(100)
    t2.add(15)
    t2.add(160)
    t2.add(125)

    actual = t.tree_intersection(t2)
    expect = []

    assert actual == expect
