from arrays.two_sum import two_sum


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([2, 4, 1000, 0], 1002) == (0, 1)
