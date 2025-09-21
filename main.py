
special_char = "!@#$%^&*()<>?,.:;" # variable that hold special characters that need to be present in password


def password_checker(password): # reusable code that can be called upon 

    issues = []

    has_uppercase = any(char.isupper() for char in password) # checks the password for any uppercase letter if any is found it returns True

    has_lowercase = any(char.islower() for char in password)

    has_digit = any(char.isdigit() for char in password)

    has_special = any(char in special_char for char in password)

    if len(password) < 8: 
        issues.append("Must be a minimum of 8 characters long.")

    if not has_uppercase:
        issues.append("Password must contain at least one uppercase letter.")
    
    if not has_lowercase:
        issues.append("Password must contain at least one lowercase letter.")
    
    if not has_digit:
        issues.append("Password must contain at least one digit.")

    if not has_special:
        issues.append("Password must contain at least one special character.")

    elif has_uppercase and has_lowercase and has_digit and has_special and len(password) >= 8:
        return "Strong Password: password meets all criteria", []

    return "Weak password", issues

while True: # loops through the password checker until user decides to quit
    password = input("Enter a password to check strength (or type 'q' to quit): ") # asks for the user input - regarding password

    if password.lower() == "q":
        break
    

    strength, issues = password_checker(password) # run password_checker here

    print("Strenght: ", strength)

    for x in issues: # a loop that runs thru issues one at a time
        print("Suggestions - ", x)