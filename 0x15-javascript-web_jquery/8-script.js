$(document).ready(() => {
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/films/?format=json",
		method: 'GET',
		dataType: 'json',
		success: (data) => {
			const films = data.results;
			for (let film of films) {
				$('UL#list_movies').append(`<li>${film.title}</li>`);
			}
		},
		error: () => {
			$('UL#list_movies').text('fail to load moves');
		}
	});
});
