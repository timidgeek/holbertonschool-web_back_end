// task one - recieve input from cmd line
const readline = require('readline');

// create interface for interacting w/ cmd line
const cli = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// prompt for user input
cli.question('Welcome to Holberton School, what is your name?' + '\n', (name) => {
  // process user input
  console.log(`Your name is: ${name}`);
  // add an exit message when closing the readline interface
  cli.close();
  process.stdout.write('This important software is now closing\n');
});
