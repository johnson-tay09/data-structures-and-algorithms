from merge_sort import merge_sort


def test_zero():
    z = []
    actual = merge_sort(z)
    expected = "Not a valid input"
    assert actual == expected


def test_one():
    z = [1]
    actual = merge_sort(z)
    expected = [1]
    assert actual == expected


def test_many():
    z = [8, 4, 23, 42, 16, 15]
    actual = merge_sort(z)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_many1():
    z = [20, 18, 12, 8, 5, -2]
    actual = merge_sort(z)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_many2():
    z = [5, 12, 7, 5, 5, 7]
    actual = merge_sort(z)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_many3():
    z = [2, 3, 5, 7, 13, 11]
    actual = merge_sort(z)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
