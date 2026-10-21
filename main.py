import random

print("=== My First Python Project ===")

while True:
    input("Press Enter to generate a number...")
    number = random.randint(1, 100)
    print(f"Your random number is: {number}")

    again = input("Try again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break