#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
const secArg = parseInt(process.argv[3]);

function add (firstArg, secArg) {
  const result = firstArg + secArg;
  console.log(result);
}
add(firstArg, secArg);
