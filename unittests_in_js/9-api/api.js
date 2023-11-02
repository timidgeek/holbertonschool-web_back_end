// task nine - regex testing
const express = require('express');
const app = express();

module.exports = app
  .get('/', (req, res) => {
    res.send('Welcome to the payment system');
  })
  .get('/cart/:id', (req, res) => {
    const id = req.params.id;
    if (isNaN(id)) {
      res.status(404).send('id must be a number');
    } else {
      res.send(`Payment methods for cart ${id}`);
    }
  })
  .listen(7865, () => {
    console.log('API available on localhost port 7865');
  });
