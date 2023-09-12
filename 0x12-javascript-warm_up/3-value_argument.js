#!/usr/bin/node

const firstArgument = process.argv[2];

if (process.argv[2]) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
