#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    results = [
        f"{a} + {b} = {add(a, b)}",
        f"{a} - {b} = {sub(a, b)}",
        f"{a} * {b} = {mul(a, b)}",
        f"{a} / {b} = {div(a, b)}"
    ]

    for result in results:
        print(result)
