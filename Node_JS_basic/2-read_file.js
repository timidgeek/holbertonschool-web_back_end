// task two - countStudents using database.csv
// imports
const fs = require('fs');

module.exports = function countStudents(path) {
  //  connects to `database.csv` to grab info
  // const path = 'database.csv';

  try {
    // read database file synchronously
    const db = fs.readFileSync(path, 'utf8');
    // create list for students
    // const students = [];

    // parse the CSV data
    let data = db.split('\n');
    data = data.filter((line) => line !== '').slice(1);

    // if database is available, log numStudents
    console.log(`Number of students: ${data.length}`);

    // log number of students in each field in special format
    const fields = {};
    for (const line of data) {
      if (line) {
        const student = line.split(',');
        if (!fields[student[3]]) {
          fields[student[3]] = [];
        }
        fields[student[3]].push(student[0]);
      }
    }

    for (const field in fields) {
      if (field) {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
