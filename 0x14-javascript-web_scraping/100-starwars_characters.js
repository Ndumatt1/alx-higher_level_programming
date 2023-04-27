#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    data.forEach((data) => {
      request.get(data, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
