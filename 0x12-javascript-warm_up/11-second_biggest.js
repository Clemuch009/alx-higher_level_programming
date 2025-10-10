#!/usr/bin/node

let list = process.argv.slice(2);

if (list.length === 0)
{
	console.log('0');
}


else
{
	let big = list[0];
	for (let num of list)
	{
		if (num > big)
		{
			big = num;
		}
	}
	console.log(big);
}
