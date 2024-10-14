from parentheses import matching_parentheses
import pytest



@pytest.mark.parametrize('string', ["((()))()", "(())()", "()"])
def test_has_matching(string):
    assert matching_parentheses(string), f"{string} has matching parentheses"

@pytest.mark.parametrize('string', ["((())", "())", "(", "(("])
def test_does_not_have_matching(string):
    assert not matching_parentheses(string), f"{string} does not have matching parentheses"

