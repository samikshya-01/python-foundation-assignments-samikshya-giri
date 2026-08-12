"""
Exercise: Data Quality Checker
Student: Samikshya Giri
Day: 1
"""

# Input values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Calculations
# Assumption: missing_rows and duplicate_rows do not overlap
problematic_rows = missing_rows + duplicate_rows
problem_percentage = (problematic_rows / total_rows) * 100

# Classification
if problem_percentage <= 2:
    classification = "Excellent"
elif problem_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

# Output
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f}%")
print(f"Classification: {classification}")