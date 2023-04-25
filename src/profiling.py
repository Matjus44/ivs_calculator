import math_library
import sys

# Set condition to false which will be usefull later.
error_invalid_data = False
# Reading lines from data file.
lines = sys.stdin.readlines()

# Spaces and tabulators will be ingored, numbers will be stored in list.
lines = [line.strip() for line in lines]

# Split each line into a list of numbers.
numbers_list = []
for line in lines:
    numbers_list.extend(line.split())

# Gets count of numbers in list
amount_of_numbers = len(numbers_list)    

# If the data file was empty, then we consider it as error because we can not make next calculations without data.
if amount_of_numbers == 0:
    print("inserted data file is empty")
    sys.exit()

##
# @Brief We loop trough number in data and we check if each string represents a number.
# If there is some string which does not represent number, then we break the loop and in next function we kill the program.
# @param amount_of_numbers
#
for i in range(amount_of_numbers):
    try:
        numbers_list[i] = float(numbers_list[i])
    except ValueError:
        error_invalid_data = True
        break
##
# @brief If there was error above, then kill the program with error message.
#
if error_invalid_data == True:
    print("In data.txt file is some invalide character, u can use only numbers!")
    sys.exit()
##
# @brief adds nubmers from data together and return its value.
# @param amount_of_numbers
# @param number_list
# @return final_result
#
def adding_numbers(amount_of_numbers,number_list):
    final_result = 0
    for i in range(amount_of_numbers):
        number = float(number_list[i])
        final_result = math_library.add(final_result, number)
    return final_result

result = adding_numbers(amount_of_numbers,numbers_list)

##
# @brief Calculates average number which were read from data.
# @param result
# @param amount_of_numbers
# @return average
#
def average(result,amount_of_numbers):
    average = math_library.divide(result,amount_of_numbers)
    return average

average_result = average(result,amount_of_numbers)

## 
# @brief Calculates standard derivation
# @param average_result
# @param result
# @param amount_of_numbers
#
def standard_deviation(average_result,result,amount_of_numbers):
    # exp sum numbers (Xi**2)
    b = math_library.exponentiate(result,2)

    # exp average number (X(average)**2)
    a = math_library.exponentiate(average_result,2)
    exp_a = a

    # mutiple amount of numbers with exponented average number (N * X(average)**2)
    something = math_library.multiple(amount_of_numbers,exp_a)

    # sub multiplied sum numbers and something (Xi**2 - (N * X(average)**2))
    ba_sub = math_library.sub(b,something)

    # sub from amount of numbers - 1 (N - 1)
    c_minus_one = amount_of_numbers - 1

    # 1/(N - 1)
    c = math_library.divide(1,c_minus_one)

    # final result without sqrt (1/(N - 1)) * (Xi**2 - (N * X(average)**2))
    abc_result = math_library.multiple(c,ba_sub)

    #final result with sqrt
    sqrt_abc = math_library.sqrt(abc_result,2)
    return sqrt_abc

# store result into variabile sd_result.
sd_result = standard_deviation(average_result,result,amount_of_numbers)
# print out result.
print("this is result of standart derivation:",sd_result)
