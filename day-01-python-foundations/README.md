# Day 1: Python Foundations

## Topics Covered

- Variables
- Data types
- String methods
- Operators
- Conditional statements

## Exercises

1. Sales Summary
2. Data Quality Checker
3. File Validator
4. Customer Record Cleaner
5. Pipeline Health Status
6. Dataset Access Decision

## How to Run

Run each file using:

```bash
python exercise-01-sales-summary.py
```

## What I Learned

I hadn't used f-strings before this assignment, so learning how {variable:.2f} works for both inserting values and formatting decimals was new for me. I also got more comfortable with how combining multiple conditions using and/or changes the outcome of if-elif-else logic, rather than checking one condition at a time.

## Challenges Faced

A little challenging part was Exercise 5, where a low failure rate but a high runtime could easily be misclassified as "Healthy" if I only checked the conditions in the wrong order. I solved it by explicitly requiring both the failure rate and runtime conditions to be true for "Healthy" status, and added a specific check to catch the case where failure rate is low but runtime is too long, so it correctly falls into "Warning" instead.