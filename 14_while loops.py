num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ?")

print("Bye")

name = input("Enter your name: ")

while name == "":
    print("You did not enter a name")
    name = input("What is your name?")
    print(f"Hello {name}")

age = int(input("Enter your age: ?"))
while age < 0:
    print("age can't be negative")
    age = int(input("Enter your age: ?"))

print(f"You are {age} years old")