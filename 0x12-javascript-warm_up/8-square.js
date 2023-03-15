#!/usr/bin/node

const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argument[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
