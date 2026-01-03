# Secure Password Generator
# Internship Project - OIBSIP
# Author: Your Name
# Description: Generates strong random passwords based on user preferences

import secrets
import string
from datetime import datetime


def get_yes_no(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ["yes", "no"]:
            return choice
        else:
            print("Please enter 'yes' or 'no'.")


def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        return None

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(f"{datetime.now()} : {password}\n")


def main():
    print("\n=== Secure Password Generator ===\n")

    while True:
        length = get_password_length()

        use_upper = get_yes_no("Include uppercase letters? (yes/no): ") == "yes"
        use_lower = get_yes_no("Include lowercase letters? (yes/no): ") == "yes"
        use_digits = get_yes_no("Include numbers? (yes/no): ") == "yes"
        use_symbols = get_yes_no("Include symbols? (yes/no): ") == "yes"

        password = generate_password(
            length, use_upper, use_lower, use_digits, use_symbols
        )

        if password is None:
            print("\nError: You must select at least one character type.\n")
            continue

        print("\n--- Generated Password ---")
        print(password)

        save_choice = get_yes_no("Do you want to save this password to a file? (yes/no): ")
        if save_choice == "yes":
            save_password(password)
            print("Password saved to 'passwords.txt'")

        again = get_yes_no("\nGenerate another password? (yes/no): ")
        if again == "no":
            print("\nThank you for using the Password Generator.")
            break


if __name__ == "__main__":
    main()
