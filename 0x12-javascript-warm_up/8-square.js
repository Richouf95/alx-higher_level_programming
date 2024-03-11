#!/usr/bin/node

const { argv } = require('node:process');

const size = parseInt(argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'x';
      }
      console.log(line);
    }
  }
}
