#!/usr/bin/node
const write = require('fs/promises');

const data = process.argv[3];
const filePath = process.argv[2];

write.writeFile(filePath, data, (err) => {
  if (err) {
    console.error(err);
  }
});
