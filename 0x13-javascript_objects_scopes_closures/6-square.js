#!/usr/bin/node

const Reactangle = require('./4-rectangle.js');

class Square extends Reactangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let y = 0; y < this.height; y++) {
      let line = '';
      for (let x = 0; x < this.width; x++) {
        (c !== undefined) ? line += c : line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Square;
