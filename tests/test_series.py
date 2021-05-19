from math_series.series import fibonacci


def test_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected


def test_nine():
  actual = fibonacci(9)
  expected = 34
  assert actual == expected

def lucTest_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected