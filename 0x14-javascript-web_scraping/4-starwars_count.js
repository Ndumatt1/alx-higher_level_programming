#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    data.forEach((data) => {
      const characters = data.characters;
      if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
