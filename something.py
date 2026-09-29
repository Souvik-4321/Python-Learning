# something.py
# A simple Python learning program

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("🐍 Welcome to Python Learning!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello, {name}! 👋")
print(f"You are {age} years old.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

numbers = [10, 20, 30, 40, 50]

print("\nNumbers:", numbers)
print("Sum:", calculate_sum(numbers))
print("Average:", calculate_sum(numbers) / len(numbers))

print("\nThanks for using the program! 🚀")