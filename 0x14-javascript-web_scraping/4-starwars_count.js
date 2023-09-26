#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let body;
let films = 0;
request(url, function (err, response, data) {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(data);
    body.results.forEach(function (output) {
      output.characters.forEach(function (alt) {
        const split = alt.split('/');
        if (split[split.length - 2] === '18') {
          films++;
        }
      });
    });
    console.log(films);
  }
});
