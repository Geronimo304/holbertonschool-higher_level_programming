#!/usr/bin/node
const argv = require('process').argv;
const av = argv.slice(2);

console.log(add(parseInt(av[0], 10), parseInt(av[1], 10)));

function add (a, b) {
  return a + b;
}
