#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

function printSquare (size) {
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    let square = '';
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      square += row + '\n' + '\n';
    }
    console.log(square);
  }
}

printSquare(squareSize);
