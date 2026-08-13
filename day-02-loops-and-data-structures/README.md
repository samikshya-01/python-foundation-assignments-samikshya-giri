# Day 2: Loops and Data Structures

## Topics Covered

- For loops and range()
- While loops and break
- Modulo operator
- Continue and isinstance()
- List comprehensions
- Dictionary comprehensions
- Set operations
- Nested dictionaries

## Exercises

1. Batch Processor
2. Retry Simulation
3. Value Cleaner
4. Sales Analysis
5. Dataset Comparison
6. Student Scores
7. Order Summary
8. Contact Book (Stretch)

## How to Run

Run each file using:

```bash
python exercise-01-batch-processor.py
```

## What I Learned

I hadn't used the modulo operator for anything beyond even/odd checks before, so using it to trigger a checkpoint every third batch in Exercise 1 was a new pattern for me. I also got more comfortable with list and dictionary comprehensions, especially seeing how the same filtering logic I wrote with a loop and continue in Exercise 3 could be rewritten in a single line.

## Challenges Faced

The Contact Book stretch exercise was the trickiest part, mainly making sure search and delete never crashed when a contact didn't exist. I solved it by always checking if the name was in the dictionary first with an if statement, before trying to access or delete it, instead of assuming the lookup would succeed.