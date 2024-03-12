#!/usr/bin/node

const SquareBase = require('./5-square.js');

class Square extends SquareBase {
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
