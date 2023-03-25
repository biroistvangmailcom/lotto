import random
import csv

with open('lotto.csv', newline='') as f:
    reader = csv.reader(f)
    historical_data = list(reader)

#Generate 5 random numbers between 1 and 90
def generate_random_numbers():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 90))
    return numbers

#Compare the new and historical sets of numbers to check for matches
def compare_numbers(new_numbers, historical_data):
    for data in historical_data:
        matches = set(new_numbers).intersection(set(data))
        if len(matches) >= 2:
            return True
    return False

#Generate new set of numbers until no matches found
def generate_unique_numbers(historical_data):
    while True:
        new_numbers = generate_random_numbers()
        if not compare_numbers(new_numbers, historical_data):
            return new_numbers

#Add historical data here. List or array of previous sets of numbers consisting of 5 integers.


#Test the program
for i in range(10):
    numbers = generate_unique_numbers(historical_data)
    print("Set", i+1, ":", numbers)
    historical_data.append(numbers)
