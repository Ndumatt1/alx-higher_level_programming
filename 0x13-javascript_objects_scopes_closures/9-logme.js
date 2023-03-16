#!/usr/bin/node

let glob = 0;
exports.logMe = function (item) {
  console.log(`${glob}: ${item}`);
  glob++;
};
