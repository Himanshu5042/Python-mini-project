import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Character groups
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Make sure password contains each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Combine all characters
    all_characters = lowercase + uppercase + numbers + symbols

    # Add remaining characters
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password
    random.shuffle(password)

    return ''.join(password)


# Main Program
print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    password = generate_password(length)

    print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number.")
