import random
import string

def password_generator(min_length, numbers= True, special = True):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special_char

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True

        if new_char in special_char:
            has_special = True
        
        meets_criteria= True
        if numbers:
            meets_criteria = has_number
        if special:
            meets_criteria = has_special and has_number
    
    return pwd



min_length =int(input("Enter the minimum length of password: "))
has_numbers = input("Do you want to include numbers? (y/n) ").lower() == 'y'
has_special = input("Do you want to include special characters? (y/n) ").lower() == 'y'
pwd = password_generator(min_length, has_numbers, has_special)
print(pwd)