#!/usr/bin/node

let largest;
let secondLargest;
let numArgs = 0;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  largest = Number(process.argv[2]);
  secondLargest = Number(process.argv[3]);
  if (largest < secondLargest) {
    [largest, secondLargest] = [secondLargest, largest];
  }
  process.argv.forEach((num) => {
    if (numArgs > 3) {
      if (Number(num) > largest) {
        [largest, secondLargest] = [Number(num), largest];
      } else if (Number(num) > secondLargest) {
        secondLargest = Number(num);
      }
    }
    numArgs++;
  });
  console.log(secondLargest);
}
