import csv

#import historical data to list
with open('lotto.csv', newline='') as f:
    reader = csv.reader(f)
    historical_data = list(reader)
    length = len(historical_data)

for i in range(length):
    data = list(map(int, i))
#print(historical_data)
print(length)





print("12 occurrence: ",historical_data.count(12))
