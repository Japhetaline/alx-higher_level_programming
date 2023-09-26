#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, res, data) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(file, data, 'utf8', function (err, body) {
      if (err) {
        console.error(err);
      }
    });
  }
});
