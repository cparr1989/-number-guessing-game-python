import random

print("Welcome to the Number Guessing Game!")
print("------------------------------------")
print("Choose a difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    max_number = 50
elif choice == "2":
    max_number = 100
elif choice == "3":
    max_number = 500
else:
    print("Invalid choice. Defaulting to Medium.")
    max_number = 100

secret_number = random.randint(1, max_number)
attempts = 0

while True:
    try:
        guess = int(input(f"Guess a number between 1 and {max_number}: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    except ValueError:
        print("Please enter a valid number.")
