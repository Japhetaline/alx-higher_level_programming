#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (q = 'X') {
    for (let k = 0; k < this.height; k++) {
      console.log(q.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
