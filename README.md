# Exception Handling & Logging

This project demonstrates robust error handling and logging in Python using built-in exceptions, custom exceptions, and the logging module. It showcases best practices for handling runtime errors, invalid input, and edge cases while keeping detailed logs for debugging.

## Features

Centralized logging to file (app.log) and console

Custom exception (NegativeNumberError)

Graceful handling of:

Division by zero

Invalid type conversions

Negative values where not allowed

Unexpected runtime errors

Use of try / except / else / finally blocks

Clear user-friendly console messages


## Functions Overview
### divide_numbers(a, b)

Divides two numbers

Handles division by zero safely

Logs success, errors, and function calls

### process_value(value)

Converts input to an integer and calculates its inverse

Handles:

Invalid integers

Division by zero

Unexpected exceptions

### sqrt_of_number(value)

Calculates the square root of a number

Raises and handles a custom NegativeNumberError

Handles invalid numeric input

### simulate_runtime_error()

Intentionally raises a RuntimeError

Demonstrates catching and logging runtime failures

### main()

Runs all demos sequentially

Acts as the program entry point

## How to Run

Make sure Python 3.x is installed
Run:
python app.py

Teaching or demonstrating defensive programming

📄 License
