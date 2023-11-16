#!/usr/bin/env node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c = 'X') {
    let symbols;
    for (let rows = 0; rows < this.height; rows++) {
      symbols = '';
      for (let cols = 0; cols < this.width; cols++) {
        symbols += c;
      }
      console.log(symbols);
    }
  }
}

module.exports = Square;
