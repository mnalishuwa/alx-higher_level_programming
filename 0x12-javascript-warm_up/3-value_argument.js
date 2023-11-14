#!/usr/bin/node

let numArgs = 0;

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  process.argv.forEach((element) => {
    if (numArgs === 2) {
      console.log(`${element}`);
    }
    numArgs++;
  });
}
