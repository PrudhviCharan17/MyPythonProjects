import time

countdown = int(input("Enter time in seconds: "))

for i in reversed(range(1, countdown+1)):
    print(i)
    time.sleep(1)

print("Time's Up")

