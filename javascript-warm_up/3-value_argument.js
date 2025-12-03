#!/usr/bin/node
const argv = require('process').argv;

console.log(argv[2] === undefined ? 'No argument' : argv[2]);
