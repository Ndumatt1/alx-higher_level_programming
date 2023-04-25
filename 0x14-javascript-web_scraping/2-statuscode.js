#!/usr/bin/node

const request = require('request');

function statusCode () {
  const url = process.argv[2];
  request.get(`${url}`, (err, response, body) => {
    if (err) console.log(err); else console.log(`code: ${response.statusCode}`);
  });
}
statusCode();
