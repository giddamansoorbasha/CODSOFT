import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length_input = input("Enter the desired password length (or 'exit' to quit): ").strip()
            if length_input.lower() == 'exit':
                print("Exiting the program.")
                break

            length = int(length_input)

            if length <= 0:
                print("Please enter a positive number.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()
