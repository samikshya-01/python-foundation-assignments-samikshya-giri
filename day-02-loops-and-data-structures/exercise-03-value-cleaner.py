"""
Exercise 3: Clean Numeric Values
Filter a list down to valid integers only, first with a loop
and continue/isinstance(), then again with a list comprehension.
"""

raw_values = [100, None, 250, "invalid", 300, None, 450]

# --- Approach 1: loop with continue and isinstance() ---
clean_values_loop = []

for value in raw_values:
    if not isinstance(value, int):
        continue
    clean_values_loop.append(value)

print("Loop version:", clean_values_loop)

# --- Approach 2: list comprehension ---
clean_values_comprehension = [value for value in raw_values if isinstance(value, int)]

print("List comprehension version:", clean_values_comprehension)