# Password Generator
# CODSOFT- Task 3

import random
import string

print("===== PASSWORD GENERATOR =====")

# Get password length from user
length = int(input("Enter the desired password length: "))

# Check if the length is valid
if length < 4:
    print("Password length should be at least 4 characters.")
else:
    # Characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display password
    print("\nGenerated Password:", password)

