#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const argument = process.argv;
const n = parseInt(argument[2]);

console.log(factorial(n));
