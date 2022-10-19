#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const result = process.argv[3];

fs.writeFile(file, result, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
