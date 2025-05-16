#!/usr/bin/node
const argv = process.argv.slice(2);
if(argv.length === 0)
{
	console.log("No argument");
}
else if( argv.length ===2)
{
	console.log(argv[0]);
	console.log(argv[1]);
}

else
{
	console.log("Enter two arguments");
}
