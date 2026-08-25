#logical operator = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be true
#                   and = both conditions must true
#                   not = inverts the conditions (not false, not true)
#or
has_candy = True
has_chocolate = False
if has_candy or has_chocolate:
    print("You have something sweet!")
else:
    print("You have no sweet!")

temp = 20
is_raining = True
if temp > 40 or temp < 0 or is_raining:
    print("The outdoor event is still scheduled")
else:
    print("The outdoor event is cancelled")

temp = 30
if temp > 40 or temp < 0:
    print("The temperature is dangerous")
else:
    print("The temperature is safe")

#and
grade = 85
submitted_project = True

if grade >= 75 and submitted_project:
    print("You passed the subject")
else:
    print("You failed the subject")


temp = 30
is_sunny = True
if temp >= 28 and is_sunny:
    print("It is a HOT outside 🥵")
    print("It is SUNNY☀️ ")
elif temp <= 0 and is_sunny:
    print("It is a COLD outside 🥶")
    print("It is SUNNY ☀️ ")
elif 28 > temp > 0 and is_sunny:
    print("It is a WARM outside 😊")
    print("It is SUNNY ☀️ ")
#not
elif temp >= 28 and not is_sunny:
    print("It is a HOT outside 🥵")
    print("It is CLOUDY 🌥️")
elif temp <= 0 and not is_sunny:
    print("It is a COLD outside 🥶")
    print("It is CLOUDY ️🌥️ ")
elif 28 > temp > 0 and not  is_sunny:
    print("It is a WARM outside 😊")
    print("It is CLOUDY 🌥️ ")

is_sleeping = True
if not is_sleeping:
    print("The person is awake")
else:
    print("the person is sleeping")

is_raining = True
if not is_raining:
    print("You can go outside")
else:
    print("Bring an umbrella")