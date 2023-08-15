#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let reappearing = 0;
  for (const data of list) {
    if (data === searchElement) {
      reappearing++;
    }
  }
  return reappearing;
};
