#!/usr/bin/env node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  list.forEach((element) => {
    if (element === searchElement) {
      occurences++;
    }
  });

  return occurences;
};