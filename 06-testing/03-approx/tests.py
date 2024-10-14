from mystatistics import average
import pytest

@pytest.mark.parametrize("ns, expected", [([0.1, 0.1, 0.1], 0.1), ([2, 3, 4], 3)])
def test_average_correct(ns, expected):
    assert pytest.approx(average(ns), abs=0.01) == expected, f"average of {ns} is indeed {expected}"