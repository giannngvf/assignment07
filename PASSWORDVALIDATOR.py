# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

import string

def display_program():
    print('This program will ask you for a password and it will only be valid if your password has characters greater than 15, one uppercase, one number, and one special character.')

def get_password():
    password = input("Enter a valid password: ")
    return password

def validity_of_password():
    lenght = len(password)
    uppercase = [True for c in password if c in string.ascii_uppercase]
    number = [True for c in password if c in string.digits]
    special_char = [True for c in password if c in string.punctuation]
    if lenght < 15:
        print('Password should have characters greater than 15.')
    elif len(uppercase) == 0:
        print('Password should contain at least one uppercase.')
    elif len(number) == 0:
        print('Password should contain at least one number.')
    elif len(special_char) == 0:
        print('Password should contain at least one special (@#$) character.')
    else:
        print('Password is valid.')

display_program() #this will just let the user know what this program is about
password = get_password() #this will ask the user for a password
validity_of_password() #this will let the user know if the password he/she input is valid; characters is greater than 15 and has at least one uppercase, one number, and one special character. 
