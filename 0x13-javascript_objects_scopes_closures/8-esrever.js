#!/usr/bin/node

exports.esrever = function (list) {
  const len = (list.length) - 1;
  const newList = [];

  for (let index = len; index >= 0; index--) {
    newList.push(list[index]);
  }
  return newList;
};
