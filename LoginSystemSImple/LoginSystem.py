from getpass import getpass

def user_prompt():
    while True:
        user_ = input("Do you want to SignUp or Login to an existing Account? ").lower().rstrip()

        if user_ == "login":
            login()
            break
        elif user_ == "signup":
            signup()
            break
        else:
            print("Invalid Input!")

def login():
    name = input("Enter Your Name: ")
    pwd = getpass(prompt="Enter Your Password: ")
    file_loc = "AccountsInfo.txt"

    if verify_login(name, pwd, file_loc):
        print(f"Welcome {name}. You have an account with us!")
    else:
        print("Account does not exist!")

def verify_login(username, password, filepath):
    password = password + '\n'

    with open(filepath, "r") as file:
        lines = file.readlines()

        for line in lines:
            fields = line.split('|')

        if(fields[0] == username and fields[1] == password):
            return True
    return False
    

def signup():
    name = input("Your Name: ")
    pwd = getpass(prompt="Make a new Password: ")

    if name == '' or pwd == '':
        print("Please enter a suitable Name or Password!")
    with open("AccountsInfo.txt", "a") as file:
        file.write(f"Account Name = {name} | Account Password = {pwd}\n")

def main():
    user_prompt()

main()