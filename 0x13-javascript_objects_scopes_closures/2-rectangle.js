#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0)) {
      // pass
    } else if ((!Number.isInteger(w)) || (!Number.isInteger(h))) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
