#!/usr/bin/node

const request = require('request');
const episodeId = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(episodeId, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
