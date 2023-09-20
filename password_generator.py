import random
import string

def generate_password(length=12):
    # Define character set (letters and digits)
    characters = string.ascii_letters + string.digits

    # Generate the password by randomly choosing characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage:
password = generate_password(8)  # Change the length as needed
print("Generated Password:", password)

