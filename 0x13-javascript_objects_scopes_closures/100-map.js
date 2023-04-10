#!/usr/bin/node

const list = require('./100-data'); // Import array from file

let newList = list.map((value, index) => value * index); // Map to compute new array

console.log("Initial list: ", list); // Print initial list
console.log("New list: ", newList); // Print new list
