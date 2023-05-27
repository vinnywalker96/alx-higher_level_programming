#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, (err, response, body) => {
  try {
    const films = JSON.parse(body).results;
    const filteredFilms = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    const numberOfMovies = filteredFilms.length;
    console.log(numberOfMovies);
  } catch (error) {
    console.error(err);
  }
});
