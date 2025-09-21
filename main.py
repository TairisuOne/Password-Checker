
special_char = "!@#$%^&*()<>?,.:;"

password = input("Enter a password to check strength: ")

def password_checker(password):

    issues = []

    has_uppercase = any(char.isupper() for char in password)

    has_lowercase = any(char.islower() for char in password)

    has_digit = any(char.isdigit() for char in password)

    has_special = any(char in special_char for char in password)

    if len(password) < 8:
        issues.append("Weak Password: too short. Must be a minimum of 8 characters long.")

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

strength, issues = password_checker(password)

print("Strenght: ", strength)

for x in issues:
    print("Suggestions - ", x)