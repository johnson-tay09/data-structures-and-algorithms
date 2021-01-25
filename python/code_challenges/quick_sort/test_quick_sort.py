from quick_sort import quick_sort


def test_zero():
    z = []
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = "Not a valid input"
    assert actual == expected


def test_one():
    z = [1]
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = [1]
    assert actual == expected


def test_many():
    z = [8, 4, 23, 42, 16, 15]
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_many1():
    z = [20, 18, 12, 8, 5, -2]
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_many2():
    z = [5, 12, 7, 5, 5, 7]
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_many3():
    z = [2, 3, 5, 7, 13, 11]
    n = len(z)
    actual = quick_sort(z, 0, n - 1)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
