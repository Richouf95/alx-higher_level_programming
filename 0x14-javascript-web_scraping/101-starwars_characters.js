#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const fetchAll = characters.map(item => {
      return new Promise((resolve, reject) => {
        request(item, function (err, res, bod) {
          if (!err && res.statusCode === 200) {
            resolve(JSON.parse(bod).name);
          } else {
            reject(new Error(err));
          }
        });
      });
    });

    Promise.all(fetchAll)
      .then(i => {
        console.log(i.join('\n'));
      })
      .catch(error => {
        console.error(error.message);
      });
  } else {
    console.error(error);
  }
});
