#!/usr/bin/node

const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);

!isNaN(myNumber) ? console.log(`My number: ${myNumber}`) : console.log('Not a number');
