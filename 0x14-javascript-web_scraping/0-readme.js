#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, content) => {
  if (err) console.error('Error reading the file:', err);
  else console.log(content);
});
