import csv
import random

filename = "random_data.csv"

headers = ["ID", "Name", "Age", "Score"]

names = ["Aarav", "Udbhaw", "Tanmayee", "Liza", "Anaya", "Piza", "Harshit", "Advika"]

rows = []

for i in range(1, 21):
    row = [
        i,
        random.choice(names),
        random.randint(18, 30),
        round(random.uniform(50, 100), 2)
    ]
    rows.append(row)

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("CSV file 'random_data.csv' successfully done!")
