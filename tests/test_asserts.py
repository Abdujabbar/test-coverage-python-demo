from coverage_demo.simple_operations import add


def test_asserts():
    assert 1, "Cool"
    assert True, "Empty"


def test_add():
    assert add(3, 4) == 3 + 4, "Invalid 1 case"
    assert add(5, 7) == 5 + 7, "Invalid 2 case"
