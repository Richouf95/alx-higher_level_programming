#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  list.forEach(x => x === searchElement && nb++);
  return nb;
};
