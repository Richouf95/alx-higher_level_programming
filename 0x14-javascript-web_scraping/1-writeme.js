#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const newLine = process.argv[3];

fs.writeFile(filePath, newLine, 'utf8', (err) => {
  if (err) console.error(err);
});
