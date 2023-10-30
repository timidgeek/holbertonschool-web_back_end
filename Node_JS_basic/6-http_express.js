// task six - http server using express
const express = require('express');

const app = express();
app
  .get('/', (req, res) => {
    res.send('Hello Holberton School!');
  })
  // server should listen on port 1245
  .listen(1245);

// export app variable
module.exports = app;
