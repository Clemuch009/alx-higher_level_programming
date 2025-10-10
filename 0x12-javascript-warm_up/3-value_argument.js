#!/usr/bin/node

let list = process.argv.slice(2);

if (list[0] !== undefined) {
	console.log(list[0]);
} else {
	console.log("No argument");
}
