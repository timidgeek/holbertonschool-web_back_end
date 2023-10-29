// task two - countStudents using database.csv
// imports
const fs = require('fs');

module.exports = function countStudents(path) {
  //  connects to `database.csv` to grab info
  // const path = 'database.csv';

  try {
    // read database file synchronously
    const db = fs.readFileSync(path, 'utf8')
    // create list for students
    const students = [];

    // parse the CSV data
    db.trim().split('\n').forEach((line) => {
      const data = line.split(',');
      if (data.length === 4) {
        const [firstName, lastName, age, field] = data;
        students.push({ firstName, lastName, age, field });
      }
    });
  
    // if database is available, log numStudents
    console.log(`Number of students: ${students.length}`);

    // log number of students in each field in special format
    const fields = {};
    students.forEach((student) => {
      if (fields[student.field]) {
        fields[student.field].count++;
        fields[student.field].list.push(student.firstName);
      } else {
        fields[student.field] = { count: 1, list: [student.firstName] };
      }
    });

    for (const field in fields) {
      console.log(`Number of students in ${field}: ${fields[field].count}. List: ${fields[field].list.join(', ')}`);
    }
  } catch (err) {
    console.error('Error: Cannot load the database');
  }
}
