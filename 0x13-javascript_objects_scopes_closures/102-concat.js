const fs = require('fs'); // Import the fs module

const file1 = process.argv[2]; // Get the first source file path from the first command line argument
const file2 = process.argv[3]; // Get the second source file path from the second command line argument
const dest = process.argv[4]; // Get the destination file path from the third command line argument

// Read the contents of the first source file
const content1 = fs.readFileSync(file1, 'utf8');

// Read the contents of the second source file
const content2 = fs.readFileSync(file2, 'utf8');

// Concatenate the two file contents
const result = content1.concat(content2);

// Write the result to the destination file
fs.writeFileSync(dest, result);

console.log(`Successfully concatenated ${file1} and ${file2} to ${dest}`);

