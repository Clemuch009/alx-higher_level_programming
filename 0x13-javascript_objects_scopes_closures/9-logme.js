#!/usr/bin/node

let count = 0;
export const logMe = function(item){
	console.log(`${count}: ${item}`);
	count++;
}
