#!/usr/bin/node

const argumentc = process.argv.length;
if (argumentc > 3) {
  console.log('Arguments found');
} else if (argumentc === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
