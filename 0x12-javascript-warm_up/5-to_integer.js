#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const convFirstArg = parseInt(firstArg);

if (!isNaN(convFirstArg)) {
  console.log('My number:', convFirstArg);
} else {
  console.log('Not a number');
}
