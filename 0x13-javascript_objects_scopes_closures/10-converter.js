#!/usr/bin/node
exports.converter = function converter (base) {
  return e => e.toString(base);
};
