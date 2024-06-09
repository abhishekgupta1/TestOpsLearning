import pytest

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_a1():
    assert 5 + 5 == 101, "Failed Test here"
        
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 1) == 0

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)        
        
        