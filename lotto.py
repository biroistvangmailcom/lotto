import random
import csv

#import historical data to list
with open('lotto.csv', newline='') as f:
    reader = csv.reader(f)
    historical_data = list(reader)

#Generate 5 random numbers between 1 and 90
def generate_random_numbers():
    numbers = []
    while len(numbers) < 5:
        number = random.randint(1, 90)

        if number not in numbers:
            numbers.append(number)

    return numbers

#Compare the new and historical sets of numbers to check for matches
def compare_numbers(new_numbers, historical_data):
    for data in historical_data:
        matches = set(new_numbers).intersection(set(data))
        if len(matches) >= 3:
            print("---------------------------------")
            print(matches)
            print(new_numbers)
            print("---------------------------------")
            return True
    return False

#Generate new set of numbers until no matches found
def generate_unique_numbers(historical_data):
    while True:
        new_numbers = generate_random_numbers()
        if not compare_numbers(new_numbers, historical_data):
            return new_numbers

#Test the program
for i in range(10):
    numbers = generate_unique_numbers(historical_data)
    print("Set", i+1, ":", numbers)
    historical_data.append(numbers)
