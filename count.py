import csv

#import historical data to list
with open('lotto.csv', newline='') as f:
    reader = csv.reader(f)
    historical_data = list(reader)
    test = historical_data[0]
    piece = test[0]


#print(historical_data)
print(type(test))
print(type(piece))
print(piece)
print(test)





print("12 occurrence: ",historical_data.count(12))
