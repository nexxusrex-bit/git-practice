# conditional expressions = A one line shortcut  for the if-else statement(ternary operator)
#                           Print or assign one of two values based on a conditions
#                           X if conditions else Y


num = 10
a = 6
b = 7
age = 18
temperature = 25
user_role = "guest"

#print("Postive" if num > 3 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "HOT" if temperature >= 30 else "COLD"
access_level = "Full access" if user_role == "Admin" else "Limited access"


print(access_level)