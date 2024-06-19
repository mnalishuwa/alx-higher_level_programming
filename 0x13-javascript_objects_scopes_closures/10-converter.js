#!/usr/bin/node

exports.converter = function (base) {
  return function (base10Number) {
    return base10Number.toString(base);
  };
};
