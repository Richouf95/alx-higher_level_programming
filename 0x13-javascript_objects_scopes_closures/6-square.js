#!/usr/bin/node

const Reactangle = require('./4-rectangle.js');

class Square extends Reactangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.height; y++) {
      let line = '';
      for (let x = 0; x < this.width; x++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
