#indexing = accessing elements of sequence using [] (indexing operator)
#                         [start : end : step]

credit_number =  "1234-5678-9012-6543"

print(credit_number[4])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[10:19])
print(credit_number[10:])

print(credit_number[-1])
print(credit_number[:])
print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number [::-1]
print(credit_number)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_initial = first_name.title()[0]
last_initial = last_name.title()[0]

print(f"Your initials are: {first_initial}.{last_initial}")