from arrays.two_sum import two_sum


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([2, 4, 1000, 0], 1002) == (0, 2)


def test_multiple_zeroes_target_zero():
    nums = [0, 0, 0]
    assert two_sum(nums, 0) == (0, 1)


def test_non_adjacent_pair_found():
    nums = [5, 2, 3, 1, 4]
    assert two_sum(nums, 6) == (0, 3)
