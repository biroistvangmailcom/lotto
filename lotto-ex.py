import pandas as pd

# Read the CSV file into a DataFrame
lottery_data = pd.read_csv("lottery.csv")

# Calculate the total number of draws
total_draws = len(lottery_data)

# Calculate the number of odd and even numbers in each draw
odd_numbers = lottery_data.iloc[:, 1:].apply(lambda x: sum(x % 2 != 0), axis=1)
even_numbers = lottery_data.iloc[:, 1:].apply(lambda x: sum(x % 2 == 0), axis=1)

# Calculate the percentage of odd and even numbers in all draws
odd_percent = round(sum(odd_numbers) / (total_draws * 5) * 100, 2)
even_percent = round(sum(even_numbers) / (total_draws * 5) * 100, 2)

print(f"Percentage of odd numbers: {odd_percent}%")
print(f"Percentage of even numbers: {even_percent}%")
