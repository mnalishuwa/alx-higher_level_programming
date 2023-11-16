#!/usr/bin/node

exports.converter = function (base) {
  return function (base10Number) {
    const hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];

    let conversion = '';
    let remainder;

    if (base10Number === 0) {
      return '0';
    }

    while (base10Number > 0) {
      remainder = base10Number % base;

      if (base === 16) {
        remainder = hexadecimal[remainder];
      }
      conversion = remainder.toString() + conversion;
      base10Number = Math.trunc(base10Number / base);
    }
    return conversion;
  };
};
