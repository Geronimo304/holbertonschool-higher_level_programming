#!/usr/bin/node
const argv = require('process').argv;

const av = argv.slice(2);

if (av.length < 1) {
  console.log('No argument');
}

if (av.length === 1) {
  console.log('Argument found');
}

if (av.length > 1) {
  console.log('Arguments found');
}
