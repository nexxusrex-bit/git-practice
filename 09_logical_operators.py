#logical operator = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be true
#                   and = both conditions must true
#                   not = inverts the conditions (not false, not true)
#or
temp = -30
is_raining = False
if temp < 40 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

#and
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
