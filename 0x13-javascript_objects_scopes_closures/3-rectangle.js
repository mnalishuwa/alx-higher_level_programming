#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbols;
    for (let rows = 0; rows < this.height; rows++) {
      symbols = '';
      for (let cols = 0; cols < this.width; cols++) {
        symbols += 'X';
      }
      console.log(symbols);
    }
  }
}

module.exports = Rectangle;
