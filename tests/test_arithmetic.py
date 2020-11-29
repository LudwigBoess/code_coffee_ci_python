from src.arithmetic import Arithmetic


def test_addition():
    arith = Arithmetic(6,4)
    assert arith.addition() == 10

def test_subtraction():
    arith = Arithmetic(6,4)
    assert arith.subtraction()== 2

def test_multiplication():
    arith = Arithmetic(6,4)
    assert arith.multiplication() == 24

def test_division():
    arith = Arithmetic(6,4)
    assert arith.division() == 1.5

