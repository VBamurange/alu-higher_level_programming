#!/usr/bin/node
const x = process.argv.length;
const y = [];

switch(x) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 2; i < x; i++) {
      y.push(process.argv[i]);
    }
    y.sort((a, b) => b - a);
    console.log(y[1]);
    break;
}
