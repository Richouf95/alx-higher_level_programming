#!/usr/bin/node

const Reactangle = require('./4-rectangle.js');

class Square extends Reactangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
