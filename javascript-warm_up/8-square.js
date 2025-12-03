#!/usr/bin/node
const argv = require('process').argv;
const size = parseInt(argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
