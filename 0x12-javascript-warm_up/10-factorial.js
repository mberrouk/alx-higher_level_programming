#!/usr/bin/node

function factorial(a) {
  if (a === 1) {
    return a;
  } else {
    return a * factorial(a - 1);
  }
}

const a = parseInt(process.argv[2]);

if (isNaN(a)) console.log(1);
else console.log(factorial(a));
