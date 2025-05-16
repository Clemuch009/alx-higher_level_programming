#!/usr/bin/node
const argv = process.argv.slice(2);

if(isNaN(argv[0]) || isNaN(argv[1]))
{
	console.log("enter valid number");

}

else
{
	const a = Number(argv[0]);
	const b = Number(argv[1]);
	add(a, b);
}

function add(a, b){
        const sum = a + b;
        console.log(sum);
        return sum;
}
