// task one - recieve input from cmd line
console.log('Welcome to Holberton School, what is your name?');
// user input event listener
process.stdin.on('readable', () => {
  const input = process.stdin.read();
  if (input) {
    process.stdout.write(`Your name is: ${input}`);
  }
});
// exit event listener
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
