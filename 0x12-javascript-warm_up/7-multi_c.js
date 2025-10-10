#!/usr/bin/node

let num = process.argv.slice(2);

if (num[0] !== undefined && !isNaN(Number(num[0]))) {
	for (let i = 0; i < Number(num[0]); i++) {
		console.log("C is fun");
	}
}
else  {
	console.log("Missing number of occurrences");
}
