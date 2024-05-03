// JavaScript script that fetches 
// and lists the title for all movies
// by using this 
//URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $('#list_movies')
    .html(data.results.map(movie => `<li>${movie.title}</li>`)
    .join(''));
});
