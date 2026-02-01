import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logger = logging.getLogger()
logger.addHandler(console_handler)


class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is not allowed."""
    pass


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero: a=%s, b=%s", a, b)
        print("Cannot divide by zero. Please provide a non-zero divisor.")
        return None
    else:
        logging.info("Division successful: %s / %s = %s", a, b, result)
        return result
    finally:
        logging.debug("divide_numbers() was called with a=%s, b=%s", a, b)


def process_value(value):
    try:
        number = int(value)
        result = 1 / number
    except ValueError:
        logging.error("ValueError: Could not convert '%s' to int", value)
        print(f"Invalid input '{value}'. Please enter a valid integer.")
        result = None
    except ZeroDivisionError:
        logging.error("ZeroDivisionError: Inversion of zero for value '%s'", value)
        print("Cannot invert zero (division by zero).")
        result = None
    except Exception:
        logging.exception("Unexpected error in process_value with value '%s'", value)
        print("An unexpected error occurred. Check logs for details.")
        result = None
    else:
        logging.info("Successfully processed value '%s'; result=%s", value, result)
    finally:
        logging.debug("process_value() finished for value '%s'", value)
        return result

def sqrt_of_number(value):
    try:
        number = float(value)
        if number < 0:
            raise NegativeNumberError(f"Negative number: {number}")
        result = number ** 0.5
    except NegativeNumberError as e:
        logging.error("NegativeNumberError: %s", e)
        print("Square root of a negative number is not allowed in this function.")
        result = None
    except ValueError as e:
        logging.error("ValueError converting '%s' to float: %s", value, e)
        print(f"Invalid number '{value}'. Please enter a valid numeric value.")
        result = None
    else:
        logging.info("sqrt_of_number successful for value=%s, result=%s", value, result)
    finally:
        logging.debug("sqrt_of_number() completed for value '%s'", value)
        return result


def simulate_runtime_error():
    try:
        logging.info("Simulating runtime error")
        raise RuntimeError("This is a simulated runtime error")
    except RuntimeError as e:
        logging.error("RuntimeError caught: %s", e)
        print("A simulated runtime error occurred. Check logs for details.")
    else:
        logging.info("No runtime error occurred in simulate_runtime_error")
    finally:
        logging.debug("simulate_runtime_error() completed")


def main():
    print("Starting error handling demo...")

    divide_numbers(10, 0)
    divide_numbers(10, 2)

    process_value("10")
    process_value("abc")
    process_value("0")

    sqrt_of_number("25")
    sqrt_of_number("-9")
    sqrt_of_number("xyz")

    simulate_runtime_error()


if __name__ == "__main__":
    main()