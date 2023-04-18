import csv
counter = 1
#import historical data to list
with open('lotto.csv', newline='') as f:
    reader = csv.reader(f)
    historical_data = list(reader)
    length = len(historical_data)
for data in historical_data[0:]:
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = int(data[3])
    data[4] = int(data[4])
    print(counter,"12 occurrence: ",data.count(12))
    counter = counter + 1
print(length)
