#!/usr/bin/node

const { argv } = require('node:process');

const first = parseInt(argv[2]);
const second = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(first, second));
