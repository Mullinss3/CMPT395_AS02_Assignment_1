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
              it returns the string "Fizz"
    
    Parameters:
              input_number - a number given to the function
    
    Returns:
              input_number - a number converted to a string that
              is not a multiple of three
              "Fizz" - a string if input_number is a multiple
              of 3
    '''    
    if (input_number == 0):
        return str(input_number)
    elif (input_number % 3 == 0):
        return "Fizz"
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
    # Testing if fizzBuzz returns a string when a number is given
    print("fizzBuzz returns a string and not a integer test:")
    str_return = fizzBuzz(0)
    is_str_return_a_str = isinstance(str_return, str)
    if (is_str_return_a_str):
        print("Pass!")
    else:
        print("Fail!")
    
    # Testing if fizzBuzz returns the string Fizz when given a multiple of three
    print("fizzBuzz returns the string Fizz when given a multiple of three test:")
    str_return = fizzBuzz(3)
    if (str_return == "Fizz"):
        print("Pass!")
    else:
        print("Fail!")
        
    # Testing if fizzBuzz does not return the string Fizz when not given a multiple of three
    print("fizzBuzz does not return the string Fizz when not given a multiple of three test:")
    str_return = fizzBuzz(2)
    if (str_return == "Fizz"):
        print("Fail!")
    else:
        print("Pass!")    

test_fizzBuzz()