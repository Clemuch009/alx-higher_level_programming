#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, resp, body) => {
	if (error) {
		console.log(error);
		return;
	}
	if (resp.statusCode == 200) {
		fs.writeFile(file, body, {encoding:'utf-8'}, (error) => {
			if (error) {
				console.log(error);
				return;
			}
			console.log('success');
		})
	}
})
