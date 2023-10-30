// task five - node http server 2.0
const http = require("http");
const countStudents = require('./3-read_file_async');

// listening on port 1245
const host = 'localhost';
const port = 1245;

// create server with http module
// assign to variable `app`
// initialization
const app = http.createServer(async (req, res) => {
  // handling paths
  if (req.url === '/') {
    res.end("Hello Holberton School!");
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
  
    // content from `3-read_file_async.js` 
    // with database name passed as argument
    await countStudents(process.argv[2])
      .then((data) => {
        const fields = Object.keys(data);

        const allStudents = fields.reduce(
          (acc, curr) => acc + data[curr].numStudents,
          0,
        );

        res.write(`Number of students: ${allStudents}\n`);

        for (let i = 0; i < fields.length; i += 1) {
          res.write(
            `Number of students in ${fields[i]}: ${
              data[fields[i]].numStudents
            }. `,
          );
          if (data[fields[i]].student) {
            // check if 'student' property is defined
            res.write(`List: ${data[fields[i]].student.join(', ')}`);
          } else {
            res.write('List: N/A');
          }    

          if (i < fields.length - 1) {
            res.write('\n');
          }
        }
      })
      .catch((err) => {
        res.write(err.message);
      })
      .finally(() => {
        res.end();
      });
  }
})
app.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});

// app must be exported
module.exports = app;
