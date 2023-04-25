#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const users = {};
    for (const todo of data) {
      if (todo.completed) {
        const userId = todo.userId;
        users[userId] = (users[userId] || 0) + 1;
      }
    }
    const result = {};
    for (const [userId, count] of Object.entries(users)) {
      result[userId] = count;
    }
    console.log(result);
  }
});
