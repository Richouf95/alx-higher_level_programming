#!/usr/bin/node

const { argv } = require('node:process');

const parsedArg = parseInt(argv[2]);

if (isNaN(parsedArg)) {
  console.log('Missing number of occurrences');
} else {
  if (parsedArg > 0) {
    for (let i = 0; i < parsedArg; i++) {
      console.log('C is fun');
    }
  }
}
