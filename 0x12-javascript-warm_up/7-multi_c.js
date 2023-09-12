#!/usr/bin/node

let firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing Number of occurrences');
} else if (firstArg > 0) {
  for (firstArg; firstArg > 0; --firstArg) {
    console.log('C is fun');
  }
}
