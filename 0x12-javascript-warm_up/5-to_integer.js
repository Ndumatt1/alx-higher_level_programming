#!/usr/bin/node
const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Not a number');
} else {
  const toInt = parseInt(argument[2]);
  console.log('My number: ' + toInt);
}
