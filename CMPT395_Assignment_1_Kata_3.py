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
    if (len(password) < 8):
        return False, "Password must be at least 8 characters"
    else:
        return True, "None"

def test_password_validator():
    '''
    Purpose:
              Runs the password_Validator function through a series of tests
    
    Parameters:
              None
    
    Returns:
              None
    '''     
    # TEST 1: Testing if password_validator recognizes string length with a success check and failure check
    print("TEST 1: Testing if password_validator recognizes string length with a success check and failure check:")    
        # password fails validation
    print("'hi' should validate False and report it is to short:")
    password_validation, password_error = password_Validator("hi")
    if (password_validation == False and password_error == "Password must be at least 8 characters"):
        print("Pass!")
    else:
        print("Fail!")
        # password succeeds validation
    password_validation, password_error = password_Validator("strongpassword")
    print("'strongpassword' should validate True and report no error:")
    if (password_validation == True and password_error == "None"):
        print("Pass!")
    else:
        print("Fail!")    
    
    
test_password_validator()