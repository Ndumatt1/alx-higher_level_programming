#!/usr/bin/node

const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Missing number of occurrences');
} else {
  const number = parseInt(argument[2]);
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
