#!/usr/bin/node

let numArgs = 0;

if (process.argv.length <= 2) {
    console.log('No argument');
} else {
    process.argv.forEach((element) => {
	if (numArgs === 2) {
	    console.log(`${element}`);
	}
	numArgs++;
    });
}
