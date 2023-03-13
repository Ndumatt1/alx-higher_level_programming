#!/usr/bin/node
function add (a, b) {
  const argument = process.argv;

  a = parseInt(argument[2]);
  b = parseInt(argument[3]);
  const result = a + b;
  console.log(result);
} add();
