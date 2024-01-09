#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  let output = '';
  for (let i = 0; i < n; i++) output += 'X';
  for (let j = 0; j < n; j++) console.log(output);
}
