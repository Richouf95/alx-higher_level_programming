#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

const fileA = fs.readFileSync(argv[2]).toString();
const fileB = fs.readFileSync(argv[3]).toString();

fs.writeFileSync(argv[4], fileA + fileB);
