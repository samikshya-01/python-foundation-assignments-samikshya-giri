"""
Exercise: File Validator
Student: Samikshya Giri
Day: 1
"""

# Allowed file extensions
allowed_extensions = (".csv", ".json", ".parquet")

# Input
file_name = input("Enter a file name: ")

# Normalize input so comparison is not case-sensitive
file_name = file_name.strip().lower()

# Validation
if file_name.endswith(allowed_extensions):
    print(f"'{file_name}' is a valid file type.")
else:
    print(f"'{file_name}' is not a valid file type. Allowed types: .csv, .json, .parquet")