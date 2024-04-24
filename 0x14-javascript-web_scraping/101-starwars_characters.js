#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.map(item => {
      return new Promise((resolve, reject) => {
        request.get(item, (error, response, characterbody) => {
          if (!err && res.statusCode === 200) {
            resolve(JSON.parse(characterbody).name);
          } else reject(new Error(error));
        });
      }).then(c => console.log(c));
    });
  } else console.error(err);
});
