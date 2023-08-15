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

  rotate () {
    const rotor = this.width;
    this.width = this.height;
    this.height = rotor;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
