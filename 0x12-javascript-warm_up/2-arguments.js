#!/usr/bin/node
'use strict';
let argv = process.argv.length;
if (argv === 2) {
    console.log('No Argument');
} else if (argv === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
