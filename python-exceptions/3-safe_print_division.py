#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.
    You have to use try: / except:
    You are not allowed to import any module.
    The result of the division should print on the finally: section,
    preceded by Inside result:

    Args:
        a: Integer
        b: Integer

    Returns: 
        The value of the division, otherwise: None
    """
    result = None  # Initialize result to None

    try:
        result = a / b
    except ZeroDivisionError:
        pass  # Do nothing, result remains None
    finally:
        print("Inside result: {}".format(result))

    return result
