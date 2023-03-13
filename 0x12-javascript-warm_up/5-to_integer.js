#!/usr/bin/node

const number = process.argv[2];
if (typeof number === 'number') {
  console.log(`My number: ${parseInt(number)}`);
} else if (typeof number === 'string' && isNaN(number) === false) {
  console.log(`My number: ${parseInt(number)}`);
} else {
  console.log('Not a number');
}
