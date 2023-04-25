import math_library as m

# Testing math library. Implementation of functions which are used here, is in math_library.py.

# Test of add function in math library.
def test_add():
    
    assert m.add(1,1) == 2
    assert m.add(100,-100) == 0
    assert m.add(-100,-100) == -200
    assert m.add(-50,75) == 25
    assert m.add(10000000,1000000) == 11000000
    assert m.add(2.6,1.7) == 4.3
    assert m.add(50.5,50) == 100.5

# Test of sub function which takes 2 numbers and subtract num2 from num1.
def test_sub():

    # without decimal numbers
    assert m.sub(1,1) == 0
    assert m.sub(5,-1) == 6
    assert m.sub(-4,1) == -5
    assert m.sub(-8,-10) == 2

    # with decimal numbers
    assert m.sub(1.0,1.5) == -0.5
    assert m.sub(5.54,-1.54) == 7.08
    assert m.sub(-2.6,5) == -7.6
    assert m.sub(-140.50,7.254) == -147.754

# Test of function multiple which takes 2 numbers and multiplies them.
def test_multiple():

    # Without decimal numbers.
    assert m.multiple(1,1) == 1
    assert m.multiple(5,-1) == -5
    assert m.multiple(-4,1) == -4
    assert m.multiple(-8,-10) == 80

    # with decimal numbers
    assert m.multiple(1.0,1.5) == 1.5
    assert m.multiple(5.55,-1.50) == -8.325
    assert m.multiple(-2.6,5) == -13
    assert m.multiple(-140.50,7.255) == -1019.3275
    assert m.multiple(-20.5,-20.5) == 420.25

# Test of function divide which divides num1 with num2.
def test_divide():

    # without decimal numbers
    assert m.divide(1,0) == m.error_divide
    assert m.divide(5,-1) == -5
    assert m.divide(-4,1) == -4
    assert m.divide(-8,-10) == 0.8

    # with decimal numbers
    assert m.divide(1.0,1.5) == 0.6666666666666666
    assert m.divide(5.55,-1.50) == -3.6999999999999997
    assert m.divide(-2.6,5) == -0.52
    assert m.divide(-140.50,7.255) == -19.365954514128187

# Test of function factorial which returns factorial of num1.
def test_factorial():
    
     # without decimal numbers
    assert m.factorial(1) == 1
    assert m.factorial(-5) == m.error_factorial
    assert m.factorial(0) == 1
    assert m.factorial(10) == 3628800

    # with decimal numbers
    assert m.factorial(1.5) == m.error_factorial
    assert m.factorial(-1.5) == m.error_factorial

# Test of function exponentiate which exponentiate num1 with num2.
def test_exponentiate():

    # without decimal numbers
    assert m.exponentiate(1,2) == 1
    assert m.exponentiate(5,2.3) == m.error_exponentiate
    assert m.exponentiate(0,10) == 0
    assert m.exponentiate(10,2) == 100

    # with decimal numbers
    assert m.exponentiate(1.5,2) == 2.25
    assert m.exponentiate(-1.5,3) == -3.375
    assert m.exponentiate(4.0,5.3) == m.error_exponentiate
    assert m.exponentiate(2.25,2) == 5.0625

# Test of square root which makes num2 square root of num1
def test_sqrt_root():

    # without decimal numbers
    assert m.sqrt(1,2) == 1
    assert m.sqrt(-5,2) == m.error_sqrt
    assert m.sqrt(0,10) == 0
    assert m.sqrt(10,2) == 3.1622776601683795

    # with decimal numbers
    assert m.sqrt(1.5,2) == 1.224744871391589
    assert m.sqrt(-2,3) == -1.2599210498948732
    assert m.sqrt(2,3) == 1.2599210498948732
    assert m.sqrt(4.0,5.3) == m.error_sqrt
    assert m.sqrt(2.25,2) == 1.5

def test_log():
    #without decimal numbers
    assert m.logarithm(2,4) == 2
    assert m.logarithm(2,-4) == m.error_log
    assert m.logarithm(-2,4) == m.error_log

    #with decimal numbers
    assert m.logarithm(2,3.5) == 1.8073549220576042
    assert m.logarithm(2,-3.5) == m.error_log
    assert m.logarithm(1.5,2) == 1.7095112913514547
    