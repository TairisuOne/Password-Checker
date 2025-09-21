
special_char = "!@#$%^&*()<>?,.:;"

password = input("Enter a password to check strength: ")

has_uppercase = any(char.isupper() for char in password)

has_lowercase = any(char.islower() for char in password)

has_digit = any(char.isdigit() for char in password)

has_special = any(char in special_char for char in password)

if len(password) < 8:
    print("Weak Password: too short")

elif has_uppercase and has_lowercase and has_digit and has_special and len(password) >= 8:
    print("Strong Password: password meets all criteria")
    
print(password)