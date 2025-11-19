#!/usr/bin/node
const request = require('request');
let id = process.argv[2];


request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
	if (error){
		console.log(error);
	}
	if (response.statusCode === 200) {
		const data = JSON.parse(body);
		console.log(data.title);
	}
}
)
