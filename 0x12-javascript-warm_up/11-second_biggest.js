#!/usr/bin/node

let res;
let args;
if (process.argv.length < 4) {
  res = 0;
} else {
  args = process.argv.slice(2).map(Number);
  args.sort((a, b) => b - a);
  res = args[1];
}
console.log(res);
