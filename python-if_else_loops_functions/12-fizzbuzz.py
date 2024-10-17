#!/usr/bin/python3

def fizzbuzz():
    output = []
    fizzbuzz_map = {
        (3, 5): "FizzBuzz",
        (3,): "Fizz",
        (5,): "Buzz"
    }

    for number in range(1, 101):
        result = ""
        for key in fizzbuzz_map:
            if all(number % k == 0 for k in key):
                result = fizzbuzz_map[key]
                break
        if result:
            output.append(result)
        else:
            output.append(str(number))

    print(" ".join(output))  # Join the list into a single string with spaces

# Example usage
if __name__ == "__main__":
    fizzbuzz()
