import string

def is_strong_password(password):
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return has_upper and has_lower and has_digit and has_special


pwd = input("Enter a password to check: ")

if is_strong_password(pwd):
    print(" Strong password!")
else:
    print(" Weak password. Use uppercase, lowercase, digits, special characters, and at least 8 characters.")