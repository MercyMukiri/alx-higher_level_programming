#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  let count = 0;
  const results = JSON.parse(body).results;

  for (const i in results) {
    const characters = results[i].characters;
    for (const j in characters) {
      if (characters[j].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
