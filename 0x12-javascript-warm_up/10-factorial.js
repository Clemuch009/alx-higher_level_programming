#!/usr/bin/node

let list = process.argv.slice(2);

function factorial(a) {
	if (a <= 1)
	{
		return 1;
	}
	return a * factorial(a - 1)
}

let num = list[0] !== undefined ? Number(list[0]) : 0;
console.log(factorial(num));
