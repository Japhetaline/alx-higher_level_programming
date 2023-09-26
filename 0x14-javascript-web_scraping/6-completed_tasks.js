#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let body;
const dictionary = {};

request(url, function (err, res, data) {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(data);
    body.forEach(function (output) {
      if (output.completed === true) {
        const userid = output.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
