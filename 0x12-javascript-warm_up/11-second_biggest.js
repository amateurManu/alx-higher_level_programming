#!/usr/bin/node
let biggest = 0;
let i;
const arrayNums = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    arrayNums[i - 2] = parseInt(process.argv[i]);
  }
}

if (arrayNums.length > 1) {
  biggest = Math.max.apply(null, arrayNums);
  i = arrayNums.indexOf(biggest);
  arrayNums[i] = -Infinity;
  biggest = Math.max.apply(null, arrayNums);
}

console.log(biggest);
