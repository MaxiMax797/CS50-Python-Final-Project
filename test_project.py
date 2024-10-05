import pytest

from project import (
    addition,
    subtraction,
    multiplication,
    division,
    square,
    cube,
    factorial_pos,
    factorial_neg,
    exp_pos,
    exp_neg,
    decimal_to_binary,
    binary_to_decimal,
    square_root,
    logarithm_base10,
    logarithm_base2,
    mtp_tables_ps,
    mtp_tables_ng
)

def test_addition():
    assert addition(3, 5) == 8
    assert addition(-1, 1) == 0
    assert addition(-1, -1) == -2
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(10, 5) == 5
    assert subtraction(5, 10) == -5
    assert subtraction(-1, -1) == 0
    assert subtraction(0, 5) == -5
    assert subtraction(0, 0) == 0

def test_multiplication():
    assert multiplication(3, 5) == 15
    assert multiplication(-1, 5) == -5
    assert multiplication(-1, -1) == 1
    assert multiplication(0, 10) == 0
    assert multiplication(0, 0) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(0, 2) == 0
    with pytest.raises(ZeroDivisionError, match="Division by zero with any number is undefined."):
        division(5, 0)
    with pytest.raises(ZeroDivisionError, match="Indeterminate form: 0/0."):
        division(0, 0)

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0

def test_factorial_pos():
    assert factorial_pos(5) == 120
    assert factorial_pos(0) == 1
    assert factorial_pos(1) == 1

def test_factorial_neg():
    assert factorial_neg(-1) == "Factorial is not defined for negative numbers."
    assert factorial_neg(-5) == "Factorial is not defined for negative numbers."

def test_exp_pos():
    assert exp_pos(2, 3) == 8
    assert exp_pos(5, 0) == 1  # Any number to the power of 0 is 1
    assert exp_pos(0, 5) == 0

def test_exp_neg():
    assert exp_neg(2, 3) == 0.125  # 2^-3 = 1/8
    assert exp_neg(5, 0) == 1  # Any number to the power of 0 is 1
    assert exp_neg(0, 5) == 0  # 0^x is 0 (for x > 0)

def test_decimal_to_binary():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(0) == "0"  # 0 in decimal is 0 in binary
    assert decimal_to_binary(255) == "11111111"
    assert decimal_to_binary(-5) == "Binary conversion is not defined for negative numbers."

def test_binary_to_decimal():
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("0") == 0
    assert binary_to_decimal("11111111") == 255
    assert binary_to_decimal("invalid") == "Invalid binary number. Please enter a valid binary string."

def test_square_root():
    assert square_root(16) == 4
    assert square_root(0) == 0
    assert square_root(25) == 5
    assert square_root(-9) == "Square root is not defined for negative numbers."

def test_logarithm_base10():
    assert logarithm_base10(100) == 2
    assert logarithm_base10(1) == 0  # log10(1) is 0
    assert logarithm_base10(10) == 1
    assert logarithm_base10(0) == "Logarithm is not defined for non-positive numbers."
    assert logarithm_base10(-5) == "Logarithm is not defined for non-positive numbers."

def test_logarithm_base2():
    assert logarithm_base2(8) == 3  # log2(8) = 3
    assert logarithm_base2(1) == 0  # log2(1) = 0
    assert logarithm_base2(0) == "Logarithm not defined for non-positive values."
    assert logarithm_base2(-5) == "Logarithm not defined for non-positive values."


def test_mtp_tables_ps():
    print("Testing mtp_tables_ps:\n")

    
    print("Test case 1: mtp_tables_ps(2, 5)")
    mtp_tables_ps(2, 5)
    print("Expected Output:\n")
    print("2 x 1 = 2")
    print("2 x 2 = 4")
    print("2 x 3 = 6")
    print("2 x 4 = 8")
    print("2 x 5 = 10\n")

    
    print("Test case 2: mtp_tables_ps(4, 3)")
    mtp_tables_ps(4, 3)
    print("Expected Output:\n")
    print("4 x 1 = 4")
    print("4 x 2 = 8")
    print("4 x 3 = 12\n")

    
    print("Test case 3: mtp_tables_ps(0, 5)")
    mtp_tables_ps(0, 5)
    print("Expected Output:\n")
    print("0 x 1 = 0")
    print("0 x 2 = 0")
    print("0 x 3 = 0")
    print("0 x 4 = 0")
    print("0 x 5 = 0\n")


def test_mtp_tables_ng():
    print("Testing mtp_tables_ng:\n")

    
    print("Test case 1: mtp_tables_ng(3, -5)")
    mtp_tables_ng(3, -5)
    print("Expected Output:\n")
    print("3 x -1 = -3")
    print("3 x -2 = -6")
    print("3 x -3 = -9")
    print("3 x -4 = -12")
    print("3 x -5 = -15\n")

    
    print("Test case 2: mtp_tables_ng(-2, -4)")
    mtp_tables_ng(-2, -4)
    print("Expected Output:\n")
    print("-2 x -1 = 2")
    print("-2 x -2 = 4")
    print("-2 x -3 = 6")
    print("-2 x -4 = 8\n")

    
    print("Test case 3: mtp_tables_ng(5, -3)")
    mtp_tables_ng(5, -3)
    print("Expected Output:\n")
    print("5 x -1 = -5")
    print("5 x -2 = -10")
    print("5 x -3 = -15\n")

if __name__ == "__main__":
    pytest.main(["-v"])
