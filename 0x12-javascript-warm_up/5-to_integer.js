#!/usr/bin/node

let list = process.argv.slice(2);

if (list[0] !== undefined && !isNaN(Number(list[0]))) {
	console.log(`My number: ${Number(list[0])}`);
} else {
	console.log("Not a number");
}
