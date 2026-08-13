"""
Exercise 5: Dataset Comparison
Compare two sets of dataset names using set operations.
"""

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

all_unique = dataset_a | dataset_b   # union
in_both = dataset_a & dataset_b      # intersection
only_in_a = dataset_a - dataset_b    # difference
only_in_b = dataset_b - dataset_a    # difference

print("All unique dataset names:", all_unique)
print("Datasets found in both groups:", in_both)
print("Datasets only in dataset_a:", only_in_a)
print("Datasets only in dataset_b:", only_in_b)