# text_cleaner.py
# Cleans a text file by removing extra spaces and empty lines (including inside lines)

import re

input_file = "messy_text.txt"
output_file = "clean_text.txt"

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    cleaned = []
    for line in lines:
        # Strip leading/trailing spaces
        line = line.strip()
        if line:  # keep only non-empty lines
            # Replace multiple spaces inside the line with a single space
            line = re.sub(r"\s+", " ", line)
            cleaned.append(line)

    with open(output_file, "w") as file:
        for line in cleaned:
            file.write(line + "\n")

    print("Text cleaned! Check:", output_file)

except FileNotFoundError:
    print("Input file not found. Please create 'messy_text.txt' in the same folder.")
