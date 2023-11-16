#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];

  for (let idx = list.length - 1; idx >= 0; idx--) {
    reversed.push(list[idx]);
  }

  return reversed;
};
