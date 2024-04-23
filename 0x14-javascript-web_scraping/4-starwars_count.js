#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (!err) {
    const result = JSON.parse(body).results;
    const numberOfMovies = result.reduce((count, movies) => {
      return movies.characters.find((c) => c.endsWith('/18/')) ? count + 1 : count;
    }, 0);
    console.log(numberOfMovies);
  }
});
