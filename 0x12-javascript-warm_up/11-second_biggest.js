#!/usr/bin/node

let arr = []; 
if (process.argv.length <= 3) {
  console.log(0);
} else {
    for (let i = 0; i < process.argv; i++) {
	  console.log(process.argv[i]);
}

console.log(arr);
