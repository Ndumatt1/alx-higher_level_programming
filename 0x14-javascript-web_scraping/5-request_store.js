#!/usr/bin/node

const fs = require('fs');
const request = require('request');

function requestStore () {
  const url = process.argv[2];
  const path = process.argv[3];
  request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      fs.writeFile(path, body, (err, data => {
        if (err) { console.log(err); }
      }));
    }
  });
}
requestStore();
