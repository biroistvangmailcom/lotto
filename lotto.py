import random
import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
            if len(matches) == 4:
                print(bcolors.WARNING + "---------------------------------")
                print(len(matches) , (matches))
                print(new_numbers)
                print(bcolors.WARNING + "---------------------------------")
            elif len(matches) == 5:
                print(bcolors.FAIL + "---------------------------------")
                print(len(matches) , (matches))
                print(new_numbers)
                print(bcolors.FAIL + "---------------------------------")
            print(bcolors.OKBLUE + "---------------------------------")
            print(len(matches) , (matches))
            print(new_numbers)
            print(bcolors.OKBLUE + "---------------------------------")
            return True
    return False

#Generate new set of numbers until no matches found
def generate_unique_numbers(historical_data):
    while True:
        new_numbers = generate_random_numbers()
        if not compare_numbers(new_numbers, historical_data):
            return new_numbers

#Test the program
for i in range(100):
    numbers = generate_unique_numbers(historical_data)
    print(bcolors.OKGREEN + "Set", i+1, ":", numbers)
    historical_data.append(numbers)
