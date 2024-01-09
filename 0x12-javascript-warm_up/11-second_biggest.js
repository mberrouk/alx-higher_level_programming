#!/usr/bin/node

const arg = process.argv;
let res = NaN;
let tmp;

arg.forEach((val, index) => {
  if (!isNaN(tmp = parseInt(val)) && (isNaN(res) || res < tmp)) {
    res = tmp;
  }
});

console.log(res);
