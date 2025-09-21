

password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password: too short")

if any(char.isupper() for char in password):
    print("Password Contains at least 1 uppercase letter")
print(password)