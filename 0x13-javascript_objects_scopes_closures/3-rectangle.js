#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (w <= 0)) {
      // pass
    } else if ((!Number.isInteger(w)) || (!Number.isInteger(h))) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += 'X';
      }
      console.log(`${square}`);
    }
  }
};
