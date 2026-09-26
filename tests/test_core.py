import pytest

from fibonacci_kata.core import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (10, 55),
        (20, 6765)
    ],
)

def test_cases(n, expected):
    assert fibonacci(n) == expected