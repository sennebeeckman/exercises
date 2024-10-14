import pytest
from mergesort import split_in_two, merge_sorted, merge_sort
from itertools import permutations

@pytest.mark.parametrize("n", [[range(k)] for k in range(100)])
def test_split_correctly(n):
    left, right = split_in_two(n)
    assert left + right == n
    assert abs(len(left) - len(right)) <= 1

@pytest.mark.parametrize("left", [[], [1], [1, 2, 3, 4, 5], [1, 3, 5], [2, 2, 4, 4, 5]])
@pytest.mark.parametrize("right", [[], [2], [6, 7, 8 ,9, 10], [2, 4, 6], [1, 1, 3, 3, 6]])
def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    assert actual == sorted(left+right)

@pytest.mark.parametrize("ns, expected", [(list(nx), ns) for ns in [[range(k)] for k in range(100)] for nx in permutations(ns)])
def test_merge_sort(ns, expected):
    actual = merge_sort(ns)
    assert actual == expected
