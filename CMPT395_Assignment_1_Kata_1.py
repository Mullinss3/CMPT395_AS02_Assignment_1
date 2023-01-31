# CMPT 395 Assignment 1
# Kata 1
# By Shea Mullins
'''
OBJECTIVE
1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.
Notes:
- start with the minimal failing solution
- keep the three rules in mind and always write just sufficient enough code
- do not forget to refactor your code after each passing test
- write your assertions relating to the exact requirements
2. For multiples of three return “Fizz” instead of the number
3. For the multiples of five return “Buzz”
4. For numbers that are multiples of both three and five return “FizzBuzz”.
'''

def fizzBuzz(input_number):
    '''
    Purpose:
              Takes a given number and returns it as a string, 
              if the number given is a multiple of 3, then
              it returns the string "Fizz". If the number given
              is a multiple of 5, then it returns the string
              "Buzz".
    
    Parameters:
              input_number - a number given to the function
    
    Returns:
              returns the string "Fizz" if input_number was
              a multiple of 3, "Buzz" if input_number was a
              multiple of 5, or just returns input_number as
              a string if not a multiple of 5 or 3
    '''    
    # input_number was 0
    if (input_number == 0):
        return str(input_number)
    # input_number was a multiple of 3
    elif (input_number % 3 == 0):
        return "Fizz"
    # input_number was a multiple of 5
    elif (input_number % 5 == 0):
        return "Buzz"
    # input_number was not a multiple of 3 or 5
    else:
        return str(input_number)

def test_fizzBuzz():
    '''
    Purpose:
              Runs the fizzBuzz function through a series of tests
    
    Parameters:
              None
    
    Returns:
              None
    '''     
    # TEST 1: Testing if fizzBuzz returns a string when a number is given
    print("TEST 1: fizzBuzz returns a string and not a integer test:")
    str_return = fizzBuzz(0)
    is_str_return_a_str = isinstance(str_return, str)
    if (is_str_return_a_str):
        print("Pass!")
    else:
        print("Fail!")
    
    # TEST 2: Testing if fizzBuzz returns the string 'Fizz' when given a multiple of 3
    print("TEST 2: fizzBuzz returns the string 'Fizz' when given a multiple of 3 test:")
    str_return = fizzBuzz(9)
    if (str_return == "Fizz"):
        print("Pass!")
    else:
        print("Fail!")
        
    # TEST 3: Testing if fizzBuzz returns the string 'Buzz' when given a multiple of 5
    print("TEST 3: fizzBuzz returns the string 'Buzz' when given a multiple of 5 test:")
    str_return = fizzBuzz(25)
    if (str_return == "Buzz"):
        print("Pass!")
    else:
        print("Fail!")    
        
    # TEST 4: Testing if fizzBuzz returns the number 4 as the string '4' and not 'Fizz' or 'Buzz'
    print("TEST 4: fizzBuzz returns the number 4 as the string '4' and not 'Fizz' or 'Buzz' test:")
    str_return = fizzBuzz(4)
    if (str_return == "4"):
        print("Pass!")
    else:
        print("Fail!")      

test_fizzBuzz()