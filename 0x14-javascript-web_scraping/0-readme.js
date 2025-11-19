#!/usr/bin/node

const fs = require('fs');
let file = process.argv[2];
fs.readFile(file, {"encoding":'utf-8'}, (error, data) =>{
console.log(data);
});
