#!/usr/bin/node
const argument = process.argv;

if (argument.length <= 3) {
  console.log('0');
} else {
  let max = argument[2];
  for (let i = 1; i <= argument.length; i++) {
    if (argument[i] > max) {
      max = argument[i];
    }
  }
  let secondMax = argument[2];
  for (let j = 1; j <= argument.length; j++) {
    if ((argument[j] > secondMax) && (argument[j] < max)) {
      secondMax = argument[j];
    }
  }
  console.log(secondMax);
}
