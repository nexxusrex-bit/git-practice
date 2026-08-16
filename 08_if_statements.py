#if = Do some onle IF some condition is true
#     Else(false) do something if else

online = True #True or False
if online:
    print("The user is online")
else:
    print("The user is offline")

age =int(input("Enter your age: "))
if age >= 60:
    print("You are too old to vote")
elif age >= 18:
    print("You are voted")
elif age <=18:
    print("You must be 18+ to voted")
else:
    print("You are not voted")

reponse = input("Would you food? (Y/N): ")
if reponse == "Y":
    print("Have some food")
else:
   print("Okay, no food for you!")

name = input("Enter your name: ")
if name == "":
   print("You did not enter your name")
else:
    print(f"Hello {name}!")