// task four - node http server
const http = require('http');

// listening on port 1245
const host = 'localhost';
const port = 1245;

// displays message in page body for any endpoint as plain text
const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('Hello Holberton School!');
};

// create server with http module
// assign to variable `app` - must be exported
const app = http.createServer(requestListener);
app.listen(port, host, () => {
  console.log(`Server is running on http://${host}:${port}`);
});

module.exports = app;
