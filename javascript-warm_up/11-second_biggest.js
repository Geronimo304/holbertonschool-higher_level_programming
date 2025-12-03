#!/usr/bin/node
const argv = require('process').argv;
const av = argv.slice(2).map(n => parseInt(n, 10));

if (av.length < 2) {
  console.log(0);
} else {
  const sorted = av.sort((a, b) => b - a);
  console.log(sorted[1]);
}
