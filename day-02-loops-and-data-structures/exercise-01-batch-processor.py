"""
Exercise 1: Batch Processor
Print batch numbers 1 to 10 using a for loop and range().
After every third batch, display "Checkpoint reached".
"""

for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")
    if batch_number % 3 == 0:
        print("Checkpoint reached")