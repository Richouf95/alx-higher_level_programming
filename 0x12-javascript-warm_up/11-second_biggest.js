#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(1);
} else {
  const array = [];
  for (let i = 2; i < argv.length; i++) {
    array.push(parseInt(argv[i]));
  }
  array.sort();
  console.log(array[array.length - 2]);
}
