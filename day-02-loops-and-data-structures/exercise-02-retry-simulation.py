"""
Exercise 2: Retry Simulation
Simulate a maximum of three retry attempts using a while loop.
Stop early with break if the operation succeeds.
Stretch: success is simulated on the second attempt.
"""

attempt = 1
max_attempts = 3
operation_successful = False

while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Stretch: simulate success on the second attempt
    if attempt == 2:
        operation_successful = True

    if operation_successful:
        break

    attempt += 1

if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")