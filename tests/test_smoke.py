def test_smoke():
    assert True

from calculator import calculate_exspression

def test_calculate_addition():
    assert calculate_exspression('1 + 2 + 3') == '6'

def test_calculate_subtraction():
    assert calculate_exspression('2 - 3') == '-1'

def test_smoke():
    assert True

def test_smoke1():
    assert True