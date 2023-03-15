#!/usr/bin/node

const prevSquare = require('./5-square');

class Square extends prevSquare {
  printChar (c) {
    if (c === undefined) {
      for (let i = 0; i < size; i++) {
        let newChar = '';
           for (let j = 0; j < size; j++) {
             newChar += 'X';
	  }
      console.log(`${newChar}`);
	}
	} else {
      for (let i = 0; i < this.height; i++) {
        let mainChar = '';
          for (let j = 0; j < this.width; j++) {
            mainChar += c;
		}
      console.log(`${mainChar}`);
	}
	}
  }
};

module.exports = Square;
