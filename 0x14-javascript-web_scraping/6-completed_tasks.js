#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, async (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const todos = JSON.parse(body);
    const result = {};
    todos.forEach(task => {
      if (task.completed) result[task.userId] === undefined ? result[task.userId] = 1 : result[task.userId]++;
    });
    console.log(result);
  }
});
