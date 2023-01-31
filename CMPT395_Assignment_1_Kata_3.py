# CMPT 395 AS02 Assignment 1
# Kata 3
# By Shea Mullins 3107914
'''
OBJECTIVE
Create a function that can be used as a validator for the password field
of a user registration form. The validation function takes a string as an
input and returns a validation result. The validation result should contain
a boolean indicating if the password is valid or not, and also a field with
the possible validation errors.

Requirements
1. The password must be at least 8 characters long. If it is not met, then
the following error message should be returned: “Password must be at least
8 characters”

2. The password must contain at least 2 numbers. If it is not met, then the
following error message should be returned: “The password must contain at
least 2 numbers”

3. The validation function should handle multiple validation errors.
For example, “somepassword” should an error message: “Password must be at
least 8 characters\nThe password must contain at least 2 numbers”

4. The password must contain at least one capital letter. If it is not met,
then the following error message should be returned: “password must contain
at least one capital letter”

5. The password must contain at least one special character. If it is not met,
then the following error message should be returned: “password must contain
at least one special character”
'''

def password_Validator(password):
    '''
    Purpose:
              Recieves a string input, runs it through a series of checks,
              and returns the a boolean if it passed, and any errors if it 
              did not
    
    Parameters:
              password - the string recieved as input
    
    Returns:
              True if the string passes the checks, False if it does not, and
              any failure messages if it failed a check
    '''    
    # setting up variables
    password_validation, password_error = True, None
    # checking if the password is at least 8 characters long
    if (len(password) < 8):
        password_validation, password_error = False, "Password must be at least 8 characters"
    # checking if the password has at least  two numbers
    count = 0
    for character in password:
        if (character.isnumeric()):
            count += 1
    if (count < 2):
        # password already had another validation error
        if (password_validation == False):
            password_error = password_error + "\nThe password must contain at least 2 numbers"
        # password has not errored yet
        else:
            password_validation, password_error = False, "The password must contain at least 2 numbers"
    return password_validation, password_error

def test_password_validator():
    '''
    Purpose:
              Runs the password_Validator function through a series of tests
    
    Parameters:
              None
    
    Returns:
              None
    '''     
    # TEST 1: Testing if password_validator recognizes string length and number of digits in the password with a success check
    print("TEST 1: Testing if password_validator recognizes string length and number of digits in the password with a success check:")
    # password succeeds validation
    password_validation, password_error = password_Validator("strongpassword12")
    print("'strongpassword12' should validate True and report no error:")
    if (password_validation == True and password_error == None):
        print("Pass!")
    else:
        print("Fail!")    
        
    # TEST 2: Testing if password_validator recognizes the password does not have at least 2 digits
    print("TEST 2: Testing if password_validator recognizes if the password has at least 2 digits with a success and failure check:")    
        # password fails validation
    print("'strongpassword' should validate False and report it does not have at least 2 numbers:")
    password_validation, password_error = password_Validator("strongpassword")
    if (password_validation == False and password_error == "The password must contain at least 2 numbers"):
        print("Pass!")
    else:
        print("Fail!")
    
    # TEST 3: Testing if password_validator recognizes a failure in both number of characters and digits
    print("TEST 3: Testing if password_validator recognizes a failure in both number of characters and digits:")    
        # password fails validation
    print("'hi' should validate False and report it does not have at least 8 characters and 2 numbers:")
    password_validation, password_error = password_Validator("hi")
    if (password_validation == False and password_error == "Password must be at least 8 characters\nThe password must contain at least 2 numbers"):
        print("Pass!")
    else:
        print("Fail!")       
    
    
test_password_validator()