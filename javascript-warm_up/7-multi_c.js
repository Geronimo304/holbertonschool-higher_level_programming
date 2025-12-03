#!/usr/bin/node
const argv = require('process').argv;
const times = parseInt(argv[2], 10);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
