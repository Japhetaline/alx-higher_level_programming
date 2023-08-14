#!/usr/bin/node
function factorial (digit) {
  if (digit === 0) {
    return (1);
  } else {
    return (factorial(digit - 1) * digit);
  }
}
const digit = parseInt(process.argv[2]);
if (digit) {
  const result = factorial(digit);
  console.log(result);
} else {
  console.log(1);
}
