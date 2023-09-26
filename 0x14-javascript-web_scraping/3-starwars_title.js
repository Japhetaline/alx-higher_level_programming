#!/usr/bin/node
const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let body;

request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
	body = JSON.parse(data);
    console.log(body.title);
  }
});
