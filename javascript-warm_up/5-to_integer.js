#!/usr/bin/node
const input = process.argv[2];
const number = !isNaN(parseInt(input));

if (number) {
  console.log(`My number: ${parseInt(input)}`);
} else {
  console.log('Not a number');
}
