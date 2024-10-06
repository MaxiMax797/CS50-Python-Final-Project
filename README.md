# Python Math Operations Calculator

#### Description
This scientific calculator simulator offers a user-friendly command-line interface for performing a range of math functions,  implemented in Python, using the math library.

## Overview
This project is a simple, command-line-based Python Math Operations Calculator that allows users to perform a variety of mathematical operations, such as addition, subtraction, multiplication, division, exponentiation, and many more advanced functions like logarithms, square roots, and binary conversions. It includes error handling for common issues like division by zero and invalid inputs.

---

## Features

The calculator supports the following operations:

### Basic Arithmetic:
- **Addition ('+')**
- **Subtraction ('-')**
- **Multiplication ('*')**
- **Division ('/')**

### Exponentiation:
- **Square (`**`)**
- **Cube (`***`)**
- **Exponentiation for both positive and negative powers ('exp')**

### Factorials:
- Computes the **factorial of positive numbers ('!')** and handles the error for negative numbers where factorial is undefined.

### Square Root:
- Computes the **square root ('sqrt')**. Returns an error for negative inputs as square roots of negative numbers are undefined in real numbers.

### Logarithms:
- **Base 2 logarithm ('log2')**
- **Base 10 logarithm ('log10')**
- Includes error handling for non-positive numbers since logarithms are undefined for zero or negative numbers.

### Binary and Decimal Conversion:
- **Decimal to binary conversion ('dec2bin')**
- **Binary to decimal conversion ('bin2dec')** with error handling for invalid binary strings.

### Multiplication Tables:
- Generates **multiplication tables ('mtp')** for a given number and range. Handles both positive and negative ranges.

### Advanced Error Handling:
- Handles **division by zero** and the indeterminate form '0/0'.
- Provides **user-friendly error messages** for invalid inputs (e.g., non-numeric input).

---

## How to Use

1. Ensure you have Python version 3 installed on your system.

2. Install the following libraries: math, pytest.

3. Clone or download the repository to your local machine.

4. Navigate to the directory containing the project files. 

5. Enter in the 'project.py' script. 

6. **Run the Calculator**: To start the calculator, run the Python script. The program enters a loop where you can input different mathematical operators and compute results for the provided numbers.

7. **Input Format**: After running the program:
   - Select an operator from the list (e.g., '+', '-', '*', '/', etc.);
   - Input the numbers when prompted;
   - The result will be displayed immediately. You can perform another operation or type 'exit' to close the program.

### Supported Operators:
- '+' for addition
- '-' for subtraction
- '*' for multiplication
- '/' for division
- '**' for square
- '***' for cube
- 'sqrt' for square root
- 'log2' for logarithm base 2
- 'log10' for logarithm base 10
- 'dec2bin' for decimal to binary conversion
- 'bin2dec' for binary to decimal conversion
- '!' for factorial
- 'exp' for exponentiation
- 'mtp' for multiplication tables
- Type `exit` to quit the program

---

## Example Interaction

Run the program.
Enter an operator sign:
('+', '-', '*', '/', '**', '***', 'sqrt', 'log2', 'log10', 'dec2bin', 'bin2dec', '!', 'exp', 'mtp') or type 'exit' to quit: 

Enter 1st number: 10
Enter 2nd number: 20
Result: 30.0

## Credits
- This project was implemented using the math library for a few functions
- The application logic and implementation were created by: Maximilian.

## Feedback and Contributions
Any feedback, bug reports and contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on the Github repository. 

Removed author infos & video URL
## Disclaimer
This project is for educational or recreational purposes only. The author is not responsible for any consequences resulting from the use or misuse of this software.

 
