#!/usr/bin/node

const { argv } = require('node:process');

const argvSize = argv.length;

if (argvSize === 3)
{
	console.log('Argument found');
}
else if (argvSize > 3)
{
	console.log('Arguments found');
}
else
{
	console.log('No argument');
}
