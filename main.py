


password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password: too short")

if any(char.isupper() for char in password):
    print("Password Contains at least 1 uppercase letter")

if any(char.islower() for char in password):
    print(True)

if any(char.isdigit() for char in password):
    print(True)

print(password)