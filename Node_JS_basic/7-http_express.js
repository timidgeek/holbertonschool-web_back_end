// task seven - complex http server
// using express
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app
  .get('/', (req, res) => {
    res.send('Hello Holberton School!');
  })
  .get('/students', async (req, res) => {
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
  })
  // server should listen on port 1245
  .listen(1245);

// export app variable
module.exports = app;
