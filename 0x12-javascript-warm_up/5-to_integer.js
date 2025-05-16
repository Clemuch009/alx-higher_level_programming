#!/usr/bin/node
const argv = process.argv.slice(2);
const num = Number(argv[0]);
if (isNaN(num)){
	console.log("Not a number");
}
else
{
	console.log(`My number is : ${num}`);
}
