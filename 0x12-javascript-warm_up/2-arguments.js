#!/usr/bin/node

let list = process.argv.slice(2);

if (list.length === 0){
	console.log("No argument");
} else if (list.length === 1){
	console.log("Argument found");
}
else{
	console.log("Arguments found");
}
