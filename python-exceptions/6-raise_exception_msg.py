#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Function that logs and raises a name exception with a message.

    Args:
        message: string of message to be raised.
    """
    print(f"Raising NameError with message: {message}")  # Log the message
    raise NameError(message)
