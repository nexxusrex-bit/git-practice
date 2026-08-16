#basic arithmetic operators
apple = 10
apple += 3
apple -= 2.5
apple /= 2
apple **= 2
remainder = apple % 3 #modulus operator
#print(remainder)

#Python weight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} is not recognized")
    print(f"Your weight is {round (weight, 2)} {unit}.")


#python calculator
operator = input("Enter your operator(+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is not recognized")
print(f"The result is {round (result, 2)}.")