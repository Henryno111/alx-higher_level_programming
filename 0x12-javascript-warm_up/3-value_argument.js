#!/usr/bin/node

const firstArg = process.argv[2];

if (process.argv[2]) {
	console.log(firstArg);
} else {
	console.log('No arguement');
}
