# csv_reader.py
# Reads a CSV file and prints each row

import csv

filename = "data.csv"  # make sure you have a CSV file in the same folder

try:
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found. Please place 'data.csv' in the same folder.")
