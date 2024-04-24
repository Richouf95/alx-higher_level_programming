#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request.get(character, (err, res, body) => {
        if (!err && res.statusCode === 200) console.log(JSON.parse(body).name);
      });
    });
  }
});
