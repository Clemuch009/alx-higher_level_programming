#!/usr/bin/node
const request = require('request');
const film_id = process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${film_id}`, (error, response, body) => {
	if (error) {
		console.log(error);
		return;
	}
	if (response.statusCode == 200) {
		const character_list = [];
		const film_data = JSON.parse(body);
		const characters = film_data.characters;
		let completed = 0; 
		for (let char_url of characters) {
			request.get(char_url, (error, char_resp, body) => {
				if (error) {
					console.log(error);
					return;
				}
				if (char_resp.statusCode === 200) {
					const char_data = JSON.parse(body);
					const character = char_data.name;
					character_list.push(character);
				}
			})
		}
		if (completed === characters.length) {
			for (let name of character_list) {
				 console.log(name);
			}
		}
	}
});
