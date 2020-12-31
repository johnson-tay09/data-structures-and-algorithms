from pascals_triangle import printPascal


def test_zero():
    actual = printPascal(0)
    expected = "Not a valid input"
    assert actual == expected


def test_one():
    actual = printPascal(1)
    expected = print(1)
    assert actual == expected


# def test_two():
#     actual = printPascal(2)
#     expected = print(1), print("1  1")
#     assert actual == expected


# def test_many():
#     actual = printPascal(12)
#     expected = 1
#     assert actual == expected