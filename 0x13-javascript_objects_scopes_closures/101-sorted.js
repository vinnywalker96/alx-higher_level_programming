#!/usr/bin/node

const dict = require('./101-data').dict; // Import dictionary from file

const newDict = {};

// Loop over the keys and values of the initial dictionary
for (const [userId, occurrence] of Object.entries(dict)) {
  if (occurrence in newDict) {
    // If the occurrence already exists in the new dictionary, add the userId to its list
    newDict[occurrence].push(userId);
  } else {
    // If the occurrence does not exist in the new dictionary, create a new list with the userId
    newDict[occurrence] = [userId];
  }
}

console.log(newDict); // Print the new dictionary
