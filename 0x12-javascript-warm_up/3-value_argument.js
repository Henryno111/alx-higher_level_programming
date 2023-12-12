#!/usr/bin/node

const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log('No arguement');
} else {
  console.log(firstArg);
}
