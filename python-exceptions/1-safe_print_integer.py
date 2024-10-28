#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints an integer with "{:d}".format().
    you have to use try: / except:
    you have to use "{:d}".format() to print a integer
    you are not allowed to import an module
    you are not allowed to use typ()

    Args:
        value: value to be printed

        Returns: True if value has correctly printed (it means the value is integer).otherwise, returns False.
    """
    try:
        #attempt to convert tpo integer and print 
        print("{:d}".format(int(vlue)))
    except (valueError, TypeError):
        return False
    return True
