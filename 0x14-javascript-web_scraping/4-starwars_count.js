#!/usr/bin/node
const request = require('request')

request.get('https://swapi-api.alx-tools.com/api/films/', (error, resp, body) => {
	if (error){
		console.log(error);
		return;
	}
	if (resp.statusCode === 200) {
		const data = JSON.parse(body)
		const films = data.results
		let total = 0
		for (let film of films) {
			for (let url of film.characters) {
				if (url === 'https://swapi-api.alx-tools.com/api/people/18/') {
					total += 1;
				}
			}
		}
		console.log(total);
	}
})
