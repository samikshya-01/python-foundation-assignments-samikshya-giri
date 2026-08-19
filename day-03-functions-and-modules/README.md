# Day 3: Functions and Modules

## Topics Covered

- Functions and default arguments
- Variable-length arguments (`*args`)
- Multiple return values
- Built-in functions: `min()`, `max()`, `sum()`, `sorted()`
- Variable scope and the `global` keyword
- Creating and importing custom modules
- Standard library modules: `random`, `datetime`

## Exercises

1. Simple Interest Calculator
2. Class Average
3. Analyze Numbers
4. Booking Counter
5. Temperature Report (Custom Module)

## How to Run

Open `Functions_and_Modules_Assignment_1.ipynb` in Jupyter or VS Code and run all cells in order.

## What I Learned

Working through default arguments in Exercise 1 made it click why parameter order matters. Required arguments have to come before the ones with defaults, and keyword arguments like `time=3` let you skip over defaults in the middle. Exercise 2 was my first real use of `*args`, and it was satisfying to see one function handle any number of scores without needing to know the count in advance. Building `temperature_utils.py` for Exercise 5 also tied everything together. Writing a small module, importing it back into the notebook, and combining it with `random` and `datetime` felt like a preview of how real projects are organized into separate files instead of one long script.

## Challenges Faced

The `global` keyword in Exercise 4 tripped me up at first. I forgot to declare `global total_seats_booked` inside `book_seats()` and got a local variable error instead of the counter updating. Once I understood that Python treats any variable you assign to inside a function as local unless you explicitly say otherwise, it made sense. I also had to be careful in Exercise 5 to import my own `temperature_utils` module only after saving it to disk first, otherwise Python couldn't find it.