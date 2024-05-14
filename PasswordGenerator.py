import random
import string


def generate_password (min_len, numbers, specials):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if specials:
        characters += special_char
    
    password = ''
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(password) < min_len:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            has_number = True
        if new_char in special_char:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if specials:
            meets_criteria = meets_criteria and has_special
            
    return password
    
def prompt_user():
    run = True
    include_numbers = False
    include_specials = False
    right_answers = ['y', 'Y']
    print('\t\t\t\tWelcome!')
    
    while run:
        try:
            length = int(input('What would you like the minimum length of your Password to be?: '))
            run = False
        except:
            print('Please enter a valid length!')
            
    num = input('would you like numbers to be included in your Password?\n(y for Yes/anything else for No): ')
    if num in right_answers:
        include_numbers = True
            
    spec = input('would you like special characters to be included in your Password?\n(y for Yes/anything else for No): ')
    if spec in right_answers:
        include_specials = True
            
    return print(generate_password(length, include_numbers, include_specials))
    
def main():
    prompt_user()
    
main()