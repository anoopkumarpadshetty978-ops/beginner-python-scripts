import pandas as pd

# 1️⃣ Read the Excel file
df = pd.read_excel('duplicate data of 200 people.xlsx')  # replace with your Excel file name

# Optional: see how many rows before cleaning
print("Total rows before removing duplicates:", len(df))

# 2️⃣ Remove duplicates
# If you want to remove rows that are identical in all columns:
df_cleaned = df.drop_duplicates()

# OR, if you only want to remove duplicates based on a specific column (e.g., 'Name'):
# df_cleaned = df.drop_duplicates(subset=['Name'])

# Optional: see how many rows after cleaning
print("Total rows after removing duplicates:", len(df_cleaned))

# 3️⃣ Save the cleaned data to a new Excel file
df_cleaned.to_excel('cleaned_file.xlsx', index=False)

print("Duplicates removed! New file saved as 'cleaned_file.xlsx'")