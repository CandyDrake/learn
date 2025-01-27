import pytest


def test_example_1(time_log):
    assert 1 + 1 == 2


@pytest.mark.time_calc
@pytest.mark.parametrize("input_data", [
    {'num': 4, 'num2': 6},
    {'num': 2, 'num2': 6},
    {'num': 3, 'num2': 5}
])
def test_example_2(input_data, time_log):
    assert input_data["num"] + input_data["num2"] == 8


@pytest.mark.time_calc
def test_example_3(time_log):
    assert 1 * 2 == 2


@pytest.mark.time_calc
@pytest.mark.parametrize("a, b, c", [
    (1, 1, 1),
    (2, 8, 40),
    (3, 4, 12)
])
def test_example_4(a, b, c, time_log):
    assert a * b == c
