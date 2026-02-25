# Password Strength Checker (Basic Version)

password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True


print("\n===== PASSWORD STRENGTH RESULT =====")

if length < 6:
    print("Weak Password ❌ (Too Short)")
elif has_upper and has_lower and has_digit and has_special and length >= 8:
    print("Strong Password 💪")
elif has_upper and has_lower and has_digit:
    print("Medium Password ⚠")
else:
    print("Weak Password ❌")