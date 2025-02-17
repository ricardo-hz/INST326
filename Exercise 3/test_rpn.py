from rpn import evaluate
from math import isclose
from pytest import approx
#Edge Cases
#An expression that consists of a single integer
def test_single_integer():
    assert evaluate("5") == 5.0
    
#An expression that consists of a single float
def test_single_float():
    assert evaluate("4.3") == 4.3
    
#An expression that consists of a negative number
def test_negative_number():
    assert evaluate("-2") == -2
    
#An expression that consists of a two-digit number
def test_two_digit_integer():
    assert evaluate("-5") == -5

#Happy Path Cases
#An expression that performs addition
def test_addition():
    assert evaluate("3 5 +") == 8.0

#An expression that performs subtraction
def test_subtraction():
    assert evaluate("5 3 -") == 2.0

#An expression that performs multiplication
def test_multiplication():
    assert evaluate ("10 2 *") == 20.0

#An expression that performs division
def test_division():
    assert evaluate("360 13 /") == approx(360/13)

#An expression consisting of three numbers followed by two different operators
def test_long_expression1():
    assert evaluate("235 537 28 + *") == 132775.0

#An expression consisting of two numbers, an operator, a third number, and another operator
def test_long_expression2():
    assert evaluate("56 12 * 19 /") == approx((56*12)/19)