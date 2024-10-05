import math

def addition(x, y):
    number1 = x + y
    return number1

def subtraction(x, y):
    number2 = x - y
    return number2

def multiplication(x, y):
    number3 = x * y
    return number3

def division(x, y):
    if x == 0 and y == 0:
        raise ZeroDivisionError("Indeterminate form: 0/0.")
    if y == 0:
        raise ZeroDivisionError("Division by zero with any number is undefined.")
    number4 = x / y
    return number4

def square(z):
    number5 = z * z
    return number5

def cube(z):
    number6 = z * z * z
    return number6

def square_root(z):
    if z < 0:
        return "Square root is not defined for negative numbers."
    number7 = math.sqrt(z)
    return number7

def logarithm_base2(z):
    if z <= 0:
        return "Logarithm not defined for non-positive values."
    number8 = math.log2(z)
    return number8

def logarithm_base10(z):
    if z <= 0:
        return "Logarithm is not defined for non-positive numbers."
    number9 = math.log10(z)
    return number9

def decimal_to_binary(z):
    if z < 0:
        return "Binary conversion is not defined for negative numbers."
    return bin(z)[2:]

def binary_to_decimal(z):
    try:
        return int(z, 2)
    except ValueError:
        return "Invalid binary number. Please enter a valid binary string."

def factorial_pos(z):
    number10 = 1
    for i in range(z, 1, -1):
        number10 *= i
    return number10

def factorial_neg(z):
    return "Factorial is not defined for negative numbers."

def exp_pos(base, power):
    number11 = 1
    for i in range(power):
        number11 *= base
    return number11

def exp_neg(base, power):
    if base == 0:
        return 0
    if power == 0:
        return 1
    number12 = 1
    for i in range(power):
        number12 *= base
    return 1 / number12

def mtp_tables_ps(x, y):
    print("\nResult:\n")
    for i in range(1, y + 1):
        result1 = x * i
        print(f"{x} x {i} = {result1}")
    print(f"\nThese are the multiplication tables of {x} within the range of {y}.")

def mtp_tables_ng(x, y):
    print("\nResult:\n")
    for i in range(-1, (y - 1), -1):
        result2 = x * i
        print(f"{x} x {i} = {result2}")
    print(f"\nThese are the multiplication tables of {x} within the range of {y}.")


def operator(op):
    try:
        if op == '+':
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
            print("Result:", addition(x, y))
        elif op == '-':
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
            print("Result:", subtraction(x, y))
        elif op == '*':
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
            print("Result:", multiplication(x, y))
        elif op == '/':
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
            print("Result:", division(x, y))
        elif op == '**':
            z = float(input("Enter the number to square it: "))
            print("Result:", square(z))
        elif op == '***':
            z = float(input("Enter the number to cube it: "))
            print("Result:", cube(z))
        elif op == 'sqrt':
            z = float(input("Enter the number to calculate its square root: "))
            print("Result:", square_root(z))
        elif op == 'log10':
            z = float(input("Enter the number to calculate its logarithm (base 10): "))
            print("Result:", logarithm_base10(z))
        elif op == 'log2':
            x = float(input("Enter the number to find log base 2: "))
            print("Result:", logarithm_base2(x))
        elif op == 'dec2bin':
            n = int(input("Enter the decimal number to convert to binary: "))
            print("Result:", decimal_to_binary(n))
        elif op == 'bin2dec':
            b = input("Enter the binary number to convert to decimal: ")
            print("Result:", binary_to_decimal(b))
        elif op == '!':
            z = int(input("Enter the number to calculate its factorial: "))
            if z > 0:
                print("Result:", factorial_pos(z))
            elif z < 0:
                print("Result:", factorial_neg(z))
            else:
                print("Result: 1")
        elif op == 'exp':
            b = int(input("Enter the base number: "))
            p = int(input("Enter the power number: "))
            if p < 0:
                print("Result:", exp_neg(b, abs(p)))  # Handle negative exponent
            else:
                print("Result:", exp_pos(b, p))
        elif op == "mtp":
            x = int(input("Enter the number for its multiplication tables: "))
            y = int(input("Enter the range for the tables: "))
            if y > 0:
                mtp_tables_ps(x, y)
            elif y < 0:
                mtp_tables_ng(x, y)
            else:
                print("Result:", x * y)
        else:
            print("Invalid operator!")
    except ValueError:
        print("You can only enter integers or floating point numbers. Please try again!")
    except ZeroDivisionError as e:
        if str(e) == "Indeterminate form: 0/0.":
            print("Indeterminate form: 0/0.")
        else:
            print("Any number divided by 0 is undefined.")


def main():
    while True:
        c = input("""Enter an operator sign:
                  ('+' , '-' , '*' , '/' , '**' , '***' , 'sqrt' , 'log2' , 'log10' , 'dec2bin' , 'bin2dec' ,'!' , 'exp' , 'mtp') or type 'exit' to quit:\n: """)
        if c.lower() == 'exit':
            print("The calculator is closing... \nHave a good day!\n")
            break
        operator(c)
        print()


if __name__ == "__main__":
    main()
