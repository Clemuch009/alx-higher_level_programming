const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/?format=json', (error, resp, data) => {
	console.log(data);
})
