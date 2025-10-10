#!/usr/bin/node

let list = process.argv.slice(2);

if (list[0] !== undefined && !isNaN(Number(list[0]))) {
	for (let i = 0; i < Number(list[0]); i++)
	{
		console.log('X'.repeat(Number(list[0])));
	}
} else {
	console.log("Missing size");
}
