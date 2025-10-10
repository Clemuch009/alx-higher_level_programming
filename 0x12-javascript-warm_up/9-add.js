#!/usr/bin/node
let list = process.argv.slice(2);

function add(a, b){

	console.log(Number(a) + Number(b));
}
add(list[0], list[1]);
