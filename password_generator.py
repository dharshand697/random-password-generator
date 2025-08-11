import string
import random

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Always include lowercase letters for the rest
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:  
        raise ValueError("No character types selected!")

    # First letter: always uppercase
    first_char = random.choice(string.ascii_uppercase)

    # Remaining characters: random from chosen pool
    remaining_chars = ''.join(random.choice(characters) for _ in range(length - 1))

    return first_char + remaining_chars


if __name__ == "__main__":
    print("\n--- Random Password Generator ---\n")

    try:
        length = int(input("Enter password length (e.g., 12): "))
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include special symbols? (y/n): ").lower() == 'y'
        count = int(input("How many passwords to generate? "))

        print("\nGenerated Password(s):\n")
        for _ in range(count):
            print(generate_password(length, upper, digits, symbols))

    except ValueError:
        print("Invalid input! Please enter numbers where required.")

    print("\n--- Done ---\n")
