for x in range(1, 11, 4):
    print(x)

for x in reversed(range(1, 11)):
    print(x)
print("Happy Birthday")

name = "PYTHON"
for x in reversed(name):
    print(x)

for x in range(1, 20):
    if x == 15:
        continue
    else:
        print(x)