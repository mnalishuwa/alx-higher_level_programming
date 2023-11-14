#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || (n >= 0 && n < 2)) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (process.argv.length > 2 && isNaN(Number(process.argv[2]))) {
  console.log(Number(process.argv[2]));
} else {
  factorial(Math.floor(Number(process.argv[2])));
}
