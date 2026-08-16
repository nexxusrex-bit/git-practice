#input()
name = input("What is your name?: ")
age = int(input("How old are you?: "))
birthday = input("What is your birthday?: ")
height = float(input("How tall are you?: "))
student = bool(input("Are you a student : "))

age = age + 1

print(f"Hello {name}!")
print(f"So you're gonna be {age} years old in {birthday}!")
print(f"Damn your {height} feet!")
print(f"Yes {student} i am a student!")