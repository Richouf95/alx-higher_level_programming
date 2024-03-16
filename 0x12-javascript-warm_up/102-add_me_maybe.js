#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  return theFunction(x + 1);
};
