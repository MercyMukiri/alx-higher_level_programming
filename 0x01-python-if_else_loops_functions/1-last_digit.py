#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = ((number * -1) % 10) * -1
elif number >= 0:
    last_digit = number % 10

first_string = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    print(f"{first_string} and is greater than 5")
elif last_digit == 0:
    print(f"{first_string} and is 0")
else:
    print(f"{first_string} and is less than 6 and not 0")
