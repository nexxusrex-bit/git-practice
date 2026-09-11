import time
time.sleep(1)
print("Hello World")

alarm_clock = int(input("Enter the time countdown: "))

for x in range(alarm_clock, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour}:{minutes:02}:{seconds:02d}")
    time.sleep(1)
print("TIME'S UP")