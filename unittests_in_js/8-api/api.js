// task eight - Basic Integration testing
const express = require('express');
const app = express();

module.exports = app
  .get('/', (req, res) => {
    res.send('Welcome to the payment system');
  })
  .listen(7865, () => {
    console.log('API available on localhost port 7865');
  });
