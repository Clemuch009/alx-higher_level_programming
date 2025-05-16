#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(argv[0]))
{
	console.log("enter a valid number");
}

else
{
	const n = Number(argv[0]);
	console.log(factorial(n));
}

function factorial(n){
	if (n === 0 || n === 1)  
	{
		return 1;
	}
	return n * (factorial(n - 1))
}



