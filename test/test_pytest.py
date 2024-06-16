import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add(a, b, expected):
    assert a + b == expected
