#!/usr/bin/node

function factorial(a) {
  if (isNaN(a) || a <= 0) return 1; // Return 1 if NaN or non-positive number
  return a * factorial(a - 1); // Recursive call for factorial
}

console.log(factorial(Number(process.argv[2]))); // Print the result
