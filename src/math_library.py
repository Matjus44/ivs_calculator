import math
# Error messages to print when some error appears.
error_divide = "Dividing with 0 is illegal math operation !"
error_exponentiate = "The number in exponent has to be natural number"
error_sqrt = "U can not put even number in root when you want to make square root out of negative number"
error_factorial = "Factorial can be created only from real positive numbers including 0"

##
# @biref This function takes 2 numbers and adds them together.
# @param num1
# @param num2
#
def add(num1,num2):
    return num1 + num2
##
# @brief This function takes 2 numbers and subtract num2 from num1.
# @param num1
# @param num2
#
def sub(num1,num2):
    return num1-num2
##
# @brief Takes two numbers and multiplies them.
# @param num1
# @param num2
#
def multiple(num1,num2):
    return num1*num2
##
# @brief Takes two numbers and divide num1 with number num2, num2 has to be different from 0, because dividng by 0 is illegal operation.
# @param num1
# @param num2
#
def divide(num1,num2):
    if num2 == 0:
        return error_divide
    else:
        return num1/num2
##
# @brief This function adds numbers together where after each loop is number decremented by one untill it reaches number 0.
# @param num1
#
def factorial(num1):
    if num1 < 0:
        return error_factorial
    if num1 == 0:
        return 1
    if isinstance(num1,float):
        return error_factorial
    result = 1
    while num1 > 0 :
        result = result * num1
        num1 -= 1
    
    return result
##
# @brief Takes two numbers and exponentiates num1 with num2, the number in exponentiate has to natural number, otherwise its an error.
# @param num1
# @param num2
#
def exponentiate(num1,num2):
    if isinstance(num2, float):
        return error_exponentiate

    exp_result=pow(num1,num2)
    return exp_result
##
# @brief Makes square root of number num1, if the root is even and num1 is lower then 0, then we expect error because it is an illegal operation.
# @param num1
# @param num2
# Also square root of number 0 is 0.
def sqrt(num1,num2):
    if ((num1 < 0) and (num2 % 2 == 0 )):
        return error_sqrt
    elif num1 == 0:
        return 0
    elif isinstance(num2, float):
        return error_sqrt
    else : 
        root_result = math.pow(abs(num1), 1/num2)
        if num1 < 0:
            root_result = -root_result
        return root_result


