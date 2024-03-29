#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      let line = '';
      for (let x = 0; x < this.width; x++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const w = this.width;
    const h = this.height;

    this.width = h;
    this.height = w;
  }

  double () {
    const doubleWidth = this.width * 2;
    const doubleHeight = this.height * 2;

    this.width = doubleWidth;
    this.height = doubleHeight;
  }
}

module.exports = Rectangle;
