#!/usr/bin/node

const list = require('./100-data').list; // Import array from file

let newList = list.map((value, index) => value * index); // Map to compute new array

console.log(list);
console.log(newList); 
