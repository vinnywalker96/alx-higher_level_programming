#!/usr/bin/node

const request = require('request');
const write = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const content = body;
    write.writeFile(filePath, content, (er) => {
      if (er) {
        console.log(er);
      }
    });
  }
});
