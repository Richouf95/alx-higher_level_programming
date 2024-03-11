#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);

function factorial (n) {
  if (isNaN(num)) {
    return 1;
  } else {
    return (n !== 1) ? n * factorial(n - 1) : 1;
  }
}

console.log(factorial(num));
