#!/usr/bin/node

const fs = require('fs');
function writeMe () {
  const filePath = process.argv[2];
  const stringToWrite = process.argv[3].toString();
  fs.writeFile(`${filePath}`, `${stringToWrite}`, (err, data) => {
    if (err) { console.log(`${err}`); }
  });
}

writeMe();
