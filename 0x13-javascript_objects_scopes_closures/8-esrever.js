#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let k = list.length - 1; k >= 0; k--) {
    reverse.push(list[k]);
  }
  return reverse;
};
