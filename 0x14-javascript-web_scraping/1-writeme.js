#!/usr/bin/node
const fs = require('fs');
let file = process.argv[2];
let text = process.argv[3];

fs.writeFile(file, text, (error) =>{
if (error){
console.log(error);
	return;
}
console.log("success");
})
