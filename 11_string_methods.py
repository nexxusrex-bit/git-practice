# len = length of the string

name = input("What is your name? ")

if len(name) > 12:
    print("Your name is too long.")
elif not name.find(" ") == -1:
    print("Your name must not contain spaces.")
elif not name.isalpha():
    print("Your name must not contain numbers.")
else:
    print(f"Welcome {name}")
#phone_num = input("Please enter your phone number: ")

#result = len(name)
#result = name.find("s")
#result = name.rfind("o")
#name = name.capitalize()                                                     #First letter will become upper case
#name = name.upper()                                                          #All letter become upper case
#name = name.lower()                                                          #all letter become lower case
#result = name.isdigit()                                                      #number only to be true
#result = name.isalpha()                                                       #letters only not include space to be true
#result = phone_num.count("-")                                                #count how many is the letter
#phone_num = phone_num.replace("-","")                                        #replacing the letter
#print(phone_num)

