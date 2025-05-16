#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 0 || isNaN(argv[0]))
{
	console.log("Missing number");
}

for( let x =0; x <= argv[0]; x++)
{
	console.log("C is fun");
}
