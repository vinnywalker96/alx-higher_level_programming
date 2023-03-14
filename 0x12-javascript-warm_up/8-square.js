#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Missing size');
} else if (isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
