#!/usr/bin/node

const fs = require('fs');

function readFile () {
  const filepath = process.argv[2];
  fs.readFile(`${filepath}`, { encoding: 'utf8' }, (err, data) => {
    if (err) { console.log(err); } else { console.log(`${data}`); }
  });
}
readFile();
